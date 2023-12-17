import re
from collections.abc import Callable
from decimal import Decimal

from loguru import logger
from pydantic import BaseModel


class Cotacao(BaseModel):
    nome_produto: str
    preco: Decimal
    preco_promocional: Decimal | None = None
    regra_promocao: str | None = None
    unidade_medida: str | None = None
    preco_por_unidade: Decimal | None = None

    @property
    def preco_promocao_por_unidade(self) -> Decimal | None:
        if self.preco_promocional and self.preco_por_unidade:
            return self.preco_promocional * self.preco_por_unidade / self.preco
        return None


BusinessRule = Callable[[Cotacao], None]


class Manager:
    def __init__(self, rules: list[BusinessRule] | None = None):
        self.rules = rules or []

    def handle(self, cotacao: Cotacao) -> None:
        for handle in self.rules:
            handle(cotacao)
            try:
                Cotacao.model_validate(cotacao)
            except ValueError as error:
                logger.error(error)


def calc_preco_por_unidade(cotacao: Cotacao) -> None:
    padrao = r'\s((?:\d+,)?\d+)(ml|l|g|kg)$'
    if not (result := re.findall(padrao, cotacao.nome_produto, flags=re.IGNORECASE)):
        return
    qtd, unidade = result[0]
    qtd = qtd.replace(',', '.')
    unidade = unidade.lower()
    fator = 1
    if unidade not in ('l', 'kg'):
        fator = 1000
        unidade = unidade.replace('ml', 'l').replace('g', 'kg')
    cotacao.unidade_medida = unidade
    cotacao.preco_por_unidade = cotacao.preco / Decimal(qtd) * fator

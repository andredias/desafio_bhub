import re
from collections.abc import Callable
from decimal import Decimal

from loguru import logger
from pydantic import BaseModel


class Cotacao(BaseModel):
    nome_produto: str
    preco: Decimal
    regra_promocao: str | None = None
    unidade_medida: str | None = None
    preco_por_unidade_medida: Decimal | None = None
    quantidade: float = 0
    preco_total: Decimal | None = None


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

    def handle_many(self, cotacoes: list[Cotacao]) -> None:
        for cotacao in cotacoes:
            self.handle(cotacao)


def calc_preco_total(cotacao: Cotacao) -> None:
    cotacao.preco_total = cotacao.preco * Decimal(str(cotacao.quantidade))


def calc_preco_por_unidade(cotacao: Cotacao) -> None:
    padrao = r'\s((?:\d+,)?\d+)(ml|l|g|kg)$'
    result = re.findall(padrao, cotacao.nome_produto, flags=re.IGNORECASE)
    if not result:
        return
    qtd, unidade = result[0]
    qtd = qtd.replace(',', '.')
    unidade = unidade.lower()
    fator = 1
    if unidade not in ('l', 'kg'):
        fator = 1000
        unidade = unidade.replace('ml', 'l').replace('g', 'kg')
    cotacao.unidade_medida = unidade
    cotacao.preco_por_unidade_medida = cotacao.preco / Decimal(qtd) * fator


def calc_leve_x_page_y(cotacao: Cotacao) -> None:
    """
    Leve X, pague Y
    """
    if not cotacao.regra_promocao:
        return
    padrao = r'leve\s(\d+)[,]?\spague\s(\d+)$'
    result = re.findall(padrao, cotacao.regra_promocao, flags=re.IGNORECASE)
    if not result:
        return
    leve, pague = result[0]
    leve = int(leve)
    pague = int(pague)
    assert leve > pague, 'Leve deve ser maior que pague'  # noqa: S101
    qtd_final = cotacao.quantidade - (cotacao.quantidade // leve) * (leve - pague)
    cotacao.preco_total = cotacao.preco * int(qtd_final)


def calc_deconto_sobre_quantidade(cotacao: Cotacao) -> None:
    """
    Para X unidades ou mais, desconto de Y%
    """
    if not cotacao.regra_promocao:
        return
    padrao = r'para (\d+) unidades ou mais, desconto de ((?:\d+,)?\d+)%$'
    result = re.findall(padrao, cotacao.regra_promocao, flags=re.IGNORECASE)
    if not result:
        return
    acima_de, desconto = result[0]
    acima_de = int(acima_de)
    desconto = Decimal(desconto.replace(',', '.'))
    cotacao.preco_total = cotacao.preco * int(cotacao.quantidade)
    if cotacao.quantidade >= acima_de:
        cotacao.preco_total = cotacao.preco_total * (100 - desconto) / 100


manager = Manager(
    [
        calc_preco_total,  # deve ser o primeiro da lista
        calc_preco_por_unidade,
        calc_leve_x_page_y,
        calc_deconto_sobre_quantidade,
    ]
)

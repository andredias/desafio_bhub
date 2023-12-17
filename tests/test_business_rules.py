from decimal import Decimal

from bhub.business_rules import Cotacao, calc_preco_por_unidade


def test_calc_preco_por_unidade() -> None:
    cotacao = Cotacao(nome_produto='Batata Extra kg', preco=Decimal('2.99'))
    calc_preco_por_unidade(cotacao)
    assert cotacao.preco_por_unidade is None
    assert cotacao.unidade_medida is None

    cotacao.nome_produto = '150g Queijo Mussarela'
    calc_preco_por_unidade(cotacao)
    assert cotacao.unidade_medida is None
    assert cotacao.preco_por_unidade is None

    cotacao.nome_produto = 'Chocolate 80g'
    cotacao.preco = Decimal('8.0')
    calc_preco_por_unidade(cotacao)
    assert cotacao.unidade_medida == 'kg'
    assert cotacao.preco_por_unidade == Decimal('100.0')

    cotacao = Cotacao(nome_produto='Coca-Cola 2L', preco=Decimal('10.0'))
    calc_preco_por_unidade(cotacao)
    assert cotacao.unidade_medida == 'l'
    assert cotacao.preco_por_unidade == Decimal('5.0')

    cotacao = Cotacao(nome_produto='Iogurte 300ml', preco=Decimal('2.7'))
    calc_preco_por_unidade(cotacao)
    assert cotacao.unidade_medida == 'l'
    assert cotacao.preco_por_unidade == Decimal('9.0')

    cotacao = Cotacao(nome_produto='Serotonina 30mg', preco=Decimal('10.0'))
    calc_preco_por_unidade(cotacao)
    assert cotacao.unidade_medida is None
    assert cotacao.preco_por_unidade is None

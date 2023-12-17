from decimal import Decimal

from bhub.business_rules import Cotacao, calc_leve_x_page_y, calc_preco_por_unidade


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


def test_calc_leve_x_page_y() -> None:
    cotacao = Cotacao(nome_produto='Leve 3, Pague 2', preco=Decimal('10.0'), quantidade=0)
    calc_leve_x_page_y(cotacao)
    assert cotacao.preco_total == Decimal('0')

    cotacao = Cotacao(nome_produto='Leve 3, Pague 2', preco=Decimal('10.0'), quantidade=3)
    calc_leve_x_page_y(cotacao)
    assert cotacao.preco_total == Decimal('20.0')

    cotacao = Cotacao(nome_produto='Leve 3 Pague 2', preco=Decimal('10.0'), quantidade=7)
    calc_leve_x_page_y(cotacao)
    assert cotacao.preco_total == Decimal('50.0')

    cotacao = Cotacao(nome_produto='Leve 5 Pague 3', preco=Decimal('1.0'), quantidade=10)
    calc_leve_x_page_y(cotacao)
    assert cotacao.preco_total == Decimal('6.0')

    cotacao = Cotacao(nome_produto='Leve 3, Pague 1', preco=Decimal('1.0'), quantidade=5)
    calc_leve_x_page_y(cotacao)
    assert cotacao.preco_total == Decimal('3.0')

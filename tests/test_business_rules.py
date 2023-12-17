from decimal import Decimal

from bhub.business_rules import (
    Cotacao,
    Manager,
    calc_deconto_sobre_quantidade,
    calc_leve_x_page_y,
    calc_preco_por_unidade,
    calc_preco_total,
)


def test_calc_preco_por_unidade() -> None:
    cotacao = Cotacao(nome_produto='Batata Extra kg', preco=Decimal('2.99'))
    calc_preco_por_unidade(cotacao)
    assert cotacao.preco_por_unidade_medida is None
    assert cotacao.unidade_medida is None

    cotacao.nome_produto = '150g Queijo Mussarela'
    calc_preco_por_unidade(cotacao)
    assert cotacao.unidade_medida is None
    assert cotacao.preco_por_unidade_medida is None

    cotacao.nome_produto = 'Chocolate 80g'
    cotacao.preco = Decimal('8.0')
    calc_preco_por_unidade(cotacao)
    assert cotacao.unidade_medida == 'kg'
    assert cotacao.preco_por_unidade_medida == Decimal('100.0')

    cotacao = Cotacao(nome_produto='Coca-Cola 2L', preco=Decimal('10.0'))
    calc_preco_por_unidade(cotacao)
    assert cotacao.unidade_medida == 'l'
    assert cotacao.preco_por_unidade_medida == Decimal('5.0')

    cotacao = Cotacao(nome_produto='Iogurte 300ml', preco=Decimal('2.7'))
    calc_preco_por_unidade(cotacao)
    assert cotacao.unidade_medida == 'l'
    assert cotacao.preco_por_unidade_medida == Decimal('9.0')

    cotacao = Cotacao(nome_produto='Serotonina 30mg', preco=Decimal('10.0'))
    calc_preco_por_unidade(cotacao)
    assert cotacao.unidade_medida is None
    assert cotacao.preco_por_unidade_medida is None


def test_calc_leve_x_page_y() -> None:
    cotacao = Cotacao(
        nome_produto='fubá', regra_promocao='Leve 3, Pague 2', preco=Decimal('10.0'), quantidade=0
    )
    calc_leve_x_page_y(cotacao)
    assert cotacao.descontos == Decimal('0')

    cotacao = Cotacao(
        nome_produto='fubá', regra_promocao='Leve 3, Pague 2', preco=Decimal('10.0'), quantidade=3
    )
    calc_leve_x_page_y(cotacao)
    assert cotacao.descontos == Decimal('10.0')

    cotacao = Cotacao(
        nome_produto='fubá', regra_promocao='Leve 3 Pague 2', preco=Decimal('10.0'), quantidade=7
    )
    calc_leve_x_page_y(cotacao)
    assert cotacao.descontos == Decimal('20.0')

    cotacao = Cotacao(
        nome_produto='fubá', regra_promocao='Leve 5 Pague 3', preco=Decimal('1.0'), quantidade=10
    )
    calc_leve_x_page_y(cotacao)
    assert cotacao.descontos == Decimal('4.0')

    cotacao = Cotacao(
        nome_produto='fubá', regra_promocao='Leve 3, Pague 1', preco=Decimal('1.0'), quantidade=5
    )
    calc_leve_x_page_y(cotacao)
    assert cotacao.descontos == Decimal('2.0')


def test_calc_deconto_sobre_quantidade() -> None:
    regra = 'para {} unidades ou mais, desconto de {}%'
    cotacao = Cotacao(
        nome_produto='fubá', regra_promocao=regra.format(3, 10), preco=Decimal('10.0'), quantidade=0
    )
    calc_deconto_sobre_quantidade(cotacao)
    assert cotacao.descontos == Decimal('0')

    cotacao = Cotacao(
        nome_produto='fubá', regra_promocao=regra.format(3, 10), preco=Decimal('10.0'), quantidade=2
    )
    calc_deconto_sobre_quantidade(cotacao)
    assert cotacao.descontos == Decimal('0')

    cotacao = Cotacao(
        nome_produto='fubá', regra_promocao=regra.format(3, 10), preco=Decimal('10.0'), quantidade=3
    )
    calc_deconto_sobre_quantidade(cotacao)
    assert cotacao.descontos == Decimal('3.0')

    cotacao = Cotacao(
        nome_produto='fubá', regra_promocao=regra.format(3, 10), preco=Decimal('1.0'), quantidade=10
    )
    calc_deconto_sobre_quantidade(cotacao)
    assert cotacao.descontos == Decimal('1')

    cotacao = Cotacao(
        nome_produto='fubá',
        regra_promocao=regra.format(3, '10,5'),
        preco=Decimal('10'),
        quantidade=10,
    )
    calc_deconto_sobre_quantidade(cotacao)
    assert cotacao.descontos == Decimal('10.5')


def test_calc_preco_total() -> None:
    cotacao = Cotacao(nome_produto='fubá', preco=Decimal('10.0'), quantidade=0)
    calc_preco_total(cotacao)
    assert cotacao.preco_total == Decimal('0')

    cotacao = Cotacao(nome_produto='fubá', preco=Decimal('5.99'), quantidade=2)
    calc_preco_total(cotacao)
    assert cotacao.preco_total == Decimal('11.98')

    cotacao = Cotacao(nome_produto='fubá', preco=Decimal('1.5'), quantidade=0.75)
    calc_preco_total(cotacao)
    assert cotacao.preco_total == Decimal('1.125')


def test_busines_rules_manager() -> None:
    manager = Manager(
        [
            calc_preco_total,
            calc_preco_por_unidade,
            calc_leve_x_page_y,
            calc_deconto_sobre_quantidade,
        ]
    )
    cotacoes = [
        Cotacao(
            nome_produto='Cebola Roxa Kg',
            preco=Decimal('6.0'),
            quantidade=0.75,
        ),
        Cotacao(
            nome_produto='fubá pacote 1,5Kg',
            regra_promocao='Leve 3, Pague 2',
            preco=Decimal('6.0'),
            quantidade=3,
        ),
        Cotacao(
            nome_produto='Arroz Tipo 1 5Kg',
            preco=Decimal('25.0'),
            regra_promocao='para 3 unidades ou mais, desconto de 15%',
            quantidade=2,
        ),
        Cotacao(
            nome_produto='Feijão Preto 1Kg',
            preco=Decimal('5.99'),
            regra_promocao='para 3 unidades ou mais, desconto de 15%',
            quantidade=5,
        ),
    ]
    resultados: list[dict] = [
        {
            'preco_por_unidade_medida': None,
            'unidade_medida': None,
            'preco_total': Decimal('4.5'),
            'descontos': Decimal('0'),
        },
        {
            'preco_por_unidade_medida': Decimal('4.0'),
            'unidade_medida': 'kg',
            'preco_total': Decimal('18.0'),
            'descontos': Decimal('6.0'),
        },
        {
            'preco_por_unidade_medida': Decimal('5.0'),
            'unidade_medida': 'kg',
            'preco_total': Decimal('50.0'),
            'descontos': Decimal('0'),
        },
        {
            'preco_por_unidade_medida': Decimal('5.99'),
            'unidade_medida': 'kg',
            'preco_total': Decimal('29.95'),
            'descontos': Decimal('4.4925'),
        },
    ]

    manager.handle_many(cotacoes)
    for cotacao, resultado in zip(cotacoes, resultados, strict=True):
        assert cotacao.preco_por_unidade_medida == resultado['preco_por_unidade_medida']
        assert cotacao.unidade_medida == resultado['unidade_medida']
        assert cotacao.preco_total == resultado['preco_total']

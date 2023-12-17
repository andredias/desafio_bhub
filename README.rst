Desafio Técnico do BHub
=======================

Este projeto é a implementação do desafio técnico proposto pela `BHub <https://bhub.com/>`_,
conforme documentado no arquivo ``especificacao.rst``.

Para o problema apresentado,
uma boa solução é usar o padrão de projeto ``Chain of Responsibility`` [#]_.
A solução apresentada usa uma variação dessa ideia, mas usando funções para representar as regras de negócio ao invés de classes.


Projeto de Exemplo
==================

Como exemplo de aplicação, vou apresentar parte de um projeto de cálculo de uma cotação de preços de um produto de supermercado.
Algumas das regras que devem ser aplicadas são:

#. Se o nome do produto contiver a especificação da quantidade e da unidade de medida, então deve-se calcular o preço do produto por unidade de medida. Por exemplo, para 'Refrigerante 2L' custando R$ 10, deve ser calculado o preço por litro de R$ 5.
#. Acima de 3 unidades de um mesmo produto, deve-se aplicar um desconto de 10% sobre o valor total.
#. A cada 2 unidades, a 3ª unidade é gratuita. "Leve 3, pague 2".

Novas regras podem ser adicionadas no futuro.


Instalação
==========

O projeto é baseado em Python 3.11 e usa o gerenciador de pacotes ``poetry``.
É necessário ter os dois instalados para executar o projeto.

As dependências do projeto devem ser instaladas com o comando ``poetry install``:

.. code-block:: console

    $ poetry install

O ambiente virtual deve ser ativado com o comando ``poetry shell``:

.. code-block:: console

    $ poetry shell


Descrição da Solução
====================

Como é apenas uma prova de conceito,
não há uma aplicação principal, nem banco de dados, nem uma interface gráfica.
O módulo mais importante do projeto é ``bhug/business_rules.py``, onde estão definidas as regras do negócio.
Cada regra é implementada em uma função que recebe um objeto ``Cotação`` que pode ou não ser alterado durante o processamento da regra.

A classe ``Cotação`` define atributos fornecidos tais como ``nome_produto``, ``quantidade``, ``preço`` e ``regra_promocao``.
As regras de negócio devem usar esses atributos para calcular outros atributos, como ``preço_unitario``, ``preço_total`` e ``descontos``.

A classe ``Manager`` é responsável por executar as regras em uma ou mais cotações usando os métodos ``handler`` e ``handler_many`` respectivamente.

O funcionamento das regras e do ``Manager`` estão registrados através de testes unitários no arquivo ``tests/test_business_rules.py``.
Para executar os testes, basta executar o comando ``make test`` na raiz do projeto:

.. code-block:: console

    $ make test
    pytest --cov-report term-missing --cov-report html --cov-branch \
        --cov bhub/
    ================================ test session starts =================================
    platform linux -- Python 3.11.4, pytest-7.4.3, pluggy-1.3.0
    rootdir: /home/andre/projetos/desafios_tecnicos/bhub
    configfile: pyproject.toml
    plugins: cov-4.1.0
    collected 5 items

    tests/test_business_rules.py .....                                             [100%]

    ---------- coverage: platform linux, python 3.11.4-final-0 -----------
    Name                     Stmts   Miss Branch BrPart  Cover   Missing
    --------------------------------------------------------------------
    bhub/__init__.py             0      0      0      0   100%
    bhub/business_rules.py      70      2     18      0    98%   32-33
    --------------------------------------------------------------------
    TOTAL                       70      2     18      0    98%
    Coverage HTML written to dir htmlcov


    ================================= 5 passed in 0.25s ==================================

Referências
===========

.. [#] `Design Patterns in Python: Chain of Responsibility`_

.. _`Design Patterns in Python: Chain of Responsibility`: https://medium.com/@amirm.lavasani/design-patterns-in-python-chain-of-responsibility-cc22bb241b41

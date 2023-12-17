Desafio Técnico do BHub
=======================

Este projeto é a implementação do desafio técnico proposto pela `BHub <https://bhub.com/>`_,
conforme documentado no arquivo ``especificacao.rst``.

Para o problema apresentado,
uma boa solução é usar o padrão de projeto ``Chain of Responsibility`` [#]_.

Projeto de Exemplo
==================

Como exemplo de aplicação, vou apresentar parte de um projeto de cálculo de uma cotação de preços de um produto de supermercado.
Algumas das regras que devem ser aplicadas são:

#. Se o nome do produto contiver a especificação da quantidade e da unidade de medida, então deve-se calcular o preço do produto por unidade de medida. Por exemplo, para 'Refrigerante 2L' custando R$ 10, deve ser calculado o preço por litro de R$ 5.
#. Acima de 3 unidades de um mesmo produto, deve-se aplicar um desconto de 10% sobre o valor total.
#. A cada 2 unidades, a 3ª unidade é gratuita. "Leve 3, pague 2".

Novas regras podem ser adicionadas no futuro, e a ordem de aplicação das regras pode ser alterada.


Referências
===========

.. [#] `Design Patterns in Python: Chain of Responsibility`_

.. _`Design Patterns in Python: Chain of Responsibility`: https://medium.com/@amirm.lavasani/design-patterns-in-python-chain-of-responsibility-cc22bb241b41

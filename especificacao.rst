Desafio de Solução Tech - BHub
==============================

Regras de Negócio
-----------------

Como você consegue domar um conjunto de regras de negócio que mudam o
tempo todo?

Imagine que você está escrevendo um app de processamento de pedidos para uma grande
empresa. No passado, essa empresa usava uma mistura bastante aleatória de práticas
comerciais manuais e automatizadas (de forma ad-hoc) para lidar com os pedidos; os
stakeholders agora querem juntar todas essas mais variadas maneiras de gerenciar pedidos
em um só local: seu app. No entanto, eles (e seus clientes) passaram a valorizar a
diversidade de suas regras de negócios e, portanto, dizem que você terá que trazer todas
essas regras para o novo sistema.

Na reunião com o pessoal que dá entrada nos pedidos atualmente, você descobre que suas
práticas de negócios beiram o caótico: não há duas linhas de produtos com o mesmo
conjunto de regras de processamento. Para piorar, a maioria das regras não está escrita:
muitas vezes você ouve algo como "Carol, no segundo andar, lida com esse tipo de ordem".

Durante o primeiro dia de reuniões, você decidiu se concentrar nos pagamentos e, em
particular, no processamento necessário quando um pagamento foi recebido pela empresa.
Você chega em casa exausto, com um bloco de notas cheio de trechos de regras como:

* Se o pagamento for para um produto físico, gerar uma guia de remessa para envio.
* Se o pagamento for para um livro, crie uma guia de remessa duplicada para o departamento de royalties.
* Se o pagamento for para uma nova associação de membro, ative essa associação.
* Se o pagamento for um upgrade para uma associação, aplique o upgrade.
* Se o pagamento for para uma adesão ou upgrade, envie um e-mail ao proprietário e informe-o sobre a ativação/upgrade.
* Se o pagamento for para o vídeo específico "Aprendendo a Esquiar", adicione um vídeo gratuito de "Primeiros Socorros" à guia de remessa (resultado de uma decisão judicial em 1997).
* Se o pagamento for para um produto físico ou um livro, gere um pagamento de comissão ao agente.

E assim por diante, por mais sete longas páginas. E a cada dia, para seu horror, você reúne
mais e mais páginas dessas regras.

Agora você se depara com a implementação deste sistema. As regras são complicadas e
bastante arbitrárias. Além disso, você sabe que eles vão mudar: assim que o sistema
entrar em operação, todos os tipos de casos especiais surgirão.

Objetivos
---------

1. Como você pode domar essas regras de negócios que mudam o tempo todo e novas podem surgir a qualquer momento?
2. Como você pode construir um sistema que seja flexível o suficiente para lidar com a complexidade e a necessidade dessas mudanças?
3. Como você pode fazer isso sem se condenar a vários anos de suporte ao sistema?

Solução
-------

* Codifique as partes principais de sua solução que requerem desenvolvimento interno. Procure trazer um código de qualidade que contenha testes unitários e seja fácil de entender. Fique à vontade para abstrair o que quiser.
* Traga um desenho de sua solução usando qualquer ferramenta que quiser: Miro, Google Docs, UML, diagramas genéricos, etc. Inclua também um desenho da infra-estrutura de sua aplicação
* Você pode incorporar em sua solução ferramentas de mercado prontas - no-code e low-code também são bem vindos aqui!

O que vamos avaliar?
--------------------

* Sua linha de raciocínio nas decisões que tomou para a solução do problema
* Sua organização no desenho e apresentação da solução
* Algumas possíveis soluções de arquitetura pra solução

Entrega
-------

A solução deve ser entregue por email à pessoa que está em contato durante o
processo. Se tiver código ou construir um README ou qualquer documento no Github ou
outro repositório, nos envie também o link deste.

Como será a entrevista
----------------------

1. Você compartilha de forma antecipada a solução. Se precisar de mais tempo, tente avisar com um dia de antecedência.
2. No dia da entrevista, você compartilha sua tela com o que desenvolveu/desenhou. Nós vamos te guiando para entender o seu racional.
3. Você pode:

    a. Compartilhar suas dificuldades
    b. Compartilhar coisas que você gostaria de fazer
    c. Compartilhar limitações que você teve para desenvolver
    d. Perguntar como poderíamos fazer melhor e entender o que você sabe e não sabe
    e. Levantar pontos importantes para o desenvolvimento em um time

Importante
----------

O grande objetivo aqui não é te testar e sim conhecer como você pensa e como projeta uma
solução. Além disso, se for desenvolver, use a linguagem de programação que você domina
melhor. Sintaxe é algo que aprendemos tranquilamente.

Se você não entendeu algum ponto aqui, pergunte para a pessoa que está conduzindo o
processo. Não é nenhum problema. Também não é necessário levar muito tempo nesse
teste, não tente fazer coisas que estão muito fora do seu domínio atualmente.

Tente se preparar para apresentar. Se precisar, nos pergunte como se preparar. Lembre-se,
estamos aqui para te fazer estar 100% preparado e performar bem nesse momento.
Queremos você confortável e estamos positivos com sua vinda para o nosso time. Nada é
segredo durante esse período.

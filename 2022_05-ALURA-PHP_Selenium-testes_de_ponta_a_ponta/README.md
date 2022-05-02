# PHP e Selenium: testes de ponta a ponta
>**Fonte:** Vinicius Dias<br>
>**Disponível:** <a href="https://cursos.alura.com.br/course/php-testes-end-to-end" target="_blank">ALURA</a><br>
**Conteúdo:**
- Aprenda a controlar o navegador com Selenium
- Saiba como verificar o conteúdo da resposta
- Use e submeta um formulário pelo código
- Aplica boas práticas e padrões como o PageObject
- Entenda como testar requisições AJAX
---
## 1. O que são testes E2E? Ver primeiro vídeo
### Introdução

[00:00] Sejam muito bem-vindos à Alura. Meu nome é Vinícius Dias e eu vou guiar vocês nesse treinamento de introdução aos conceitos de testes End-To-End utilizando PHP.

[00:10] Nesse treinamento, nós vamos falar, de forma bem rápida, o que é um teste End-To-End. Nós vamos ver quais problemas esse tipo de teste resolve, e vamos começar a realizar esse tipo de teste.

[00:22] E no final do treinamento, nós vamos ter mais ou menos isso aqui. Nós vamos conseguir automatizar a execução de um navegador, e eu, particularmente, acho isso muito legal, muito interessante.

[00:33] Nós vamos ver como organizar o nosso código para realizar esse tipo de teste, como atender dependências, como, por exemplo, fazer login, como você está vendo agora na tela, nós vamos ver como testar casos que demoram a ser executados utilizando Ajax.

[00:45] Nós vamos ver bastante sobre problemas que podemos esbarrar quando for realizar esse tipo de teste, mas sempre vamos conseguir contornar. Esse tipo de teste, como vou citar bastante durante o treinamento, é um tipo de teste mais lento. Repara que eu, para executar quatro testes, demorei quase vinte segundos.

[01:05] Então, é um teste lento, existem formas de otimizá-lo que eu não estou realizando, mas tem como otimizar, mas mesmo assim é um tipo de teste bem mais lento que consome bastante mais recurso. Então, é o tipo de teste que, quando falamos de pirâmide de testes, está lá no topo. É o que nós, normalmente, devemos ter menos.

[01:25] Vou falar bastante sobre isso, sobre ter menos desse tipo de teste, mas nós vamos aprender como escrever esse tipo de teste para quando ele fizer sentido.

[01:33] Então, no próximo vídeo, nós já vamos começar a entender um pouco melhor sobre esse tipo de teste, o que é esse tipo de teste, antes de botar a mão na massa. Então, espero que você tire bastante proveito, que aprenda bastante, e caso, durante o treinamento, fique com alguma dúvida, não hesite, você pode abrir uma questão lá no fórum.

[01:52] Eu tento responder pessoalmente sempre que possível, mas quando eu não consigo, a nossa comunidade de instrutores e de alunos é bastante solícita, com certeza alguém vai conseguir te ajudar.

[02:00] Então, mais uma vez, seja muito bem-vindo, obrigado por começar esse treinamento, e te espero no próximo vídeo para conversarmos um pouco sobre esse tipo de teste.

### Testes E2E

[00:00] Bem-vindos de volta. Então, antes de começarmos a colocar a mão na massa, vamos falar um pouco sobre o que vamos falar. Você provavelmente já se deparou com essa imagem aqui ou uma imagem semelhante.

<center><img src="https://caelum-online-public.s3.amazonaws.com/1851-php-testes-e2e/Transcri%C3%A7%C3%A3o/aula1_video2_imagem1.PNG"></center>

Imagem de uma pirâmide dividida em três partes: a base contém a legenda "unit", a camada do meio é "integration" e o topo possui o texto "e2e". Ao lado,há uma seta vertical que inicia na base da pirâmide com uma figura do personagem de desenho animado Papaléguas, e aponta para cima até a altura do topo da pirâmide, onde há a figura do personagem de desenho animado Coiote.

[00:13] Em algum dos treinamentos de teste, ou até mesmo no vídeo específico sobre essa imagem no vídeo na Alura+ sobre pirâmide de testes. Então, o que que acontece? Nós já vimos em treinamentos aqui sobre testes de unidade, nós já vimos sobre testes de integração, e agora nós vamos falar sobre esse topo da pirâmide aqui, que são testes End-To-End, ou seja, testes de ponta a ponta.

[00:39] Um teste de ponta a ponta é um teste que verifica o funcionamento da aplicação como um todo, ou seja, utilizando como um usuário utilizaria, acessando pelo navegador a interface da aplicação, interagindo com formulários, clicando em botões etc.

[00:56] Então, um exemplo muito simples: eu quero garantir que a página da Alura está funcionando, eu quero garantir que eu consiga acessar a página da Alura para que, depois que eu acessar, eu possa ver cursos, por exemplo.

[01:08] Então, imagina que eu tenho essa especificação aqui de funcionalidade que é “Acessar o site da Alura”. Então, eu “Como aluno quero poder acessar o site da Alura para ver quais cursos estão disponíveis”. Então, eu criei aqui um cenário de testes. Como é esse cenário?

[01:23] Eu tenho uma pré-condição, como vimos nos testes de unidade e continuou aplicando nos testes de integração, existe aquele padrão “Arrange-Act-Assert”, aquele triplo “A”, onde nós definimos, preparamos o terreno, quando executamos a ação em si, e verificamos o resultado da ação.

[01:44] Então, nós temos essas três etapas aqui, em uma linguagem um pouco mais humana, vamos dizer assim. Então, “Dado que estou com o navegador aberto”, ou seja, essa é a pré-condição, é o meu “Arrange”; “Quando visito “http://alura.com.br”, essa é a ação que eu vou executar; “Então eu vejo que o título da página contém a palavra ‘Alura’”, essa aqui é a verificação, para garantir que eu estou na página certa.

[02:06] Então, vamos realizar esse teste, vamos fazer essa verificação, esse teste de ponta a ponta. Eu estou aqui com o meu navegador aberto, antes de qualquer coisa, vou digitar “alura.com.br” e acessar.

[02:18] Então, visitei essa página e eu consigo verificar aqui no título, aqui em cima na barra do navegador, que o título contém a palavra “Alura”. Então, o que acontece? Meu teste passou. Só que como nós vimos em treinamentos anteriores, testes manuais são muito caros, são muito difíceis de fazer.

[02:37] Só que esse tipo de teste aqui envolve navegador, interface do usuário, envolve interagir com elementos, ler título. Será que conseguimos fazer isso de forma automatizada? E se você está fazendo esse curso, você provavelmente sabe que dá para fazer isso de forma automatizada, e é exatamente isso que nós vamos fazer durante esse treinamento.

[02:57] Nós vamos automatizar esse tipo de teste. Embora existam inúmeras formas de testar esse tipo de coisa, nós vamos realizar os testes de ponta a ponta controlando um navegador de verdade.

[03:10] Então, nossos testes vão abrir uma janela de navegador onde nós vamos ver cada coisa acontecendo e os testes sendo executados. Então, para isso, eu te espero no próximo vídeo para configurarmos o ambiente necessário para fazer isso tudo.

### Exercício: O que é o que é?

Já começamos de cara entendendo exatamente o que vamos testar, mas só para garantir que o conceito ficou claro:

O que é um teste E2E?

a) É um teste que abre o navegador

b) É um teste de integração entre o sistema e a interface de usuário

c) Alternativa correta: E2E (end-to-end) traduzido como ponta a ponta, testa todo o fluxo da aplicação pela perspectiva de um usuário real
- _Alternativa correta! Um teste E2E realmente utiliza a aplicação como se fosse um usuário real. Se é uma aplicação web, como no nosso caso, abre um navegador, interage com links, formulários, etc._

### Preparando o ambiente

[00:00] Bem-vindos de volta. Então, como nós já comentamos sobre o que é um teste End-To-End, vamos, finalmente, começar a configurar o nosso ambiente para poder implementar a automatização de testes End-To-End.

[00:15] Então, dando uma pesquisada em ferramentas que podem nos auxiliar nessa tarefa, eu me deparei aqui com o “php-webdriver” que, lendo a descrição, faz exatamente o que precisamos, permite que nós controlemos navegadores utilizando PHP.

[00:31] E, fica nisso, essa ferramenta serve para controlar navegadores, se você vai utilizar esse navegador para realizar testes, para fazer web scraping, para fazer o que você quiser, não importa, a ferramenta serve para isso.

[00:47] Então, nós vamos precisar dessa ferramenta aqui, então já vamos lá instalar utilizando Composer, deixa eu pegá-la, copiei, e o que que eu fiz? Eu criei um projeto vazio, ele não tem nada ainda, então, utilizando Composer, eu vou fazer o require --dev dessa ferramenta.

[01:05] E eu também vou instalar o phpunit/phpunit. Por quê? Como eu disse, essa ferramenta, esse WebDriver serve, unicamente, para controlar navegadores, e se eu quero controlar um navegador para realizar testes, faz todo sentido eu utilizar alguma ferramenta de testes para realizar minha verificação, se está tudo certo.

[01:25] Só que existem diversas ferramentas para realizar testes também, então eu vou utilizar o phpunit porque nós já conhecemos phpunit porque já temos testes de phpunit aqui. Ela não é a única ferramenta, mas é bastante utilizada, então vamos seguir com ela.

[01:42] Enquanto o Composer vai se virando aqui, enquanto ele vai procurando tudo que precisa baixar, vamos dar uma passada rápida sobre o que nós precisamos para utilizar essa ferramenta.

[01:53] Primeiro, obviamente, nós precisamos do PHP, e como você acabou de ver, nós precisamos do Composer, mas eu já estou assumindo que você tem isso instalado devido aos pré-requisitos desse treinamento.

[02:04] Então, com o PHP instalado na última versão disponível, com o Composer instalado na última versão disponível, nós vamos instalar a ferramenta necessária, que é o WebDriver, e o Composer já está fazendo isso, e nós precisamos de algo que realmente controle o navegador.

[02:19] Porque isso aqui é um código PHP que vai se comunicar com uma ferramenta, seja um navegador, seja uma outra ferramenta que controla um navegador. Então, nós temos aqui algumas possibilidades.

[02:31] Nós podemos utilizar o que é chamado de Chromedriver, que é uma ferramenta do próprio Google que vai te permitir abrir o Google Chrome e navegar entre ele; tem aqui o Geckodriver, que é basicamente a mesma coisa que o Chromedriver, mas para Firefox, ou seja, com isso vai abrir um Firefox e você vai controlar.

[02:50] E existe uma terceira opção que é utilizar uma ferramenta chamada Selenium. O que é o Selenium? O Selenium é uma ferramenta muito poderosa que te auxilia na automação de controle de navegador. E qual a diferença entre utilizar o Selenium e utilizar, por exemplo, o Chromedriver direto?

[03:10] Com o Chromedriver eu tenho uma facilidade que eu simplesmente executo esse comando aqui e já está tudo funcionando; já com o Selenium, eu tenho um servidor inteiro. Então, o Chromedriver ou o Geckodriver é um pouco mais simples, só que o Selenium traz algumas funcionalidades a mais e quando você for implementar testes End-To-End em um cenário real, já que testes End-To-End são bem mais lentos, são bem mais pesados para rodar, você muito provavelmente vai ter uma infraestrutura específica para rodar esses testes.

[03:42] Então, com o Selenium você ganha diversas funcionalidades para você conseguir ter um cluster de navegadores, por exemplo, você vai ter uma máquina rodando o Chrome e outra máquina rodando o Internet Explorer e o Selenium se comunica com as duas de forma igual. Então, tem algumas vantagens.

[04:00] Para o propósito deste treinamento, a diferença vai ser zero, mas nós já vamos se habituar com o Selenium. Então, o que vamos fazer? Vamos baixar, vamos acessar esse site do Selenium e baixar a última versão disponível estável.

[04:14] No momento da gravação desse curso, é a versão “3”, mas caso quando você estiver assistindo já tenha a versão “4” disponível, pode baixar que ela já funciona com a ferramenta que nós estamos utilizando.

[04:24] Mas eu vou baixar a versão mais estável, mais recente que é a versão “3”. Depois de baixar, nós precisamos ainda informar para o Selenium qual navegador ele vai usar. E para ele, por exemplo, automatizar o Google Chrome, ele precisa utilizar o Chromedriver; se ele vai automatizar o Firefox, ele precisa do Geckodriver.

[04:45] Então, nós precisamos informar para ele onde ele vai encontrar essa ferramenta. Então, nós subimos um pouco e acessamos a página aqui, por exemplo, do Chromedriver, que vai entregar para nós uma página.

[04:55] Você vai ver qual versão do Chrome você já tem instalada na sua máquina, então, por exemplo, eu tenho aqui sobre o Google Chrome, eu tenho a versão “83”. Então, vou vir aqui e baixar a versão do Chromedriver “83”.

[05:11] Nós vamos selecionar o nosso sistema operacional, que no meu caso é Linux, só que eu já tenho isso instalado, então eu vou extrair o arquivo executável no mesmo lugar que eu extraí o Selenium WebDriver, o Selenium server.

[05:26] Então, eu baixei aqui o Selenium, esse arquivo, baixei o Chromedriver, esse arquivo, os dois estão na mesma pasta, os dois estão aqui para mim nessa minha pasta, então, repara que eu tenho aqui o Selenium e eu tenho aqui o Chromedriver.

[05:40] Com isso, o que que eu vou fazer? O Selenium, o servidor do Selenium roda com Java, então utilizando o Java instalado na minha máquina eu vou digitar java-jar e o nome do arquivo do Selenium.

[05:52] Ele vai executar e, com isso, eu já tenho um servidor do Selenium rodando na porta “4444”. Então, vamos recapitular tudo porque eu sei que é bastante coisa.

[06:04] Eu tenho aqui uma ferramenta que se comunica com o Selenium, e nós já estamos a instalando, e junto com ela eu estou instalando o phpunit, ambas já foram instaladas aqui pelo Composer. Tenho isso instalado, está na hora de subirmos um servidor do Selenium.

[06:19] Então, nós precisamos ir lá na página do Selenium e baixar o servidor do Selenium, que é um arquivo “.jar”, só que Selenium precisa se comunicar com o Google Chrome. Então, nós vamos lá na página do Chromedriver e vamos baixá-lo também, de acordo com a versão que temos no nosso sistema instalado.

[06:38] Baixei o Chromedriver, baixei o Selenium, os dois estão na mesma pasta, eu vou levantar o servidor do Selenium – estou com dificuldade de selecionar. Então, com isso – lembrando, os dois arquivos precisam estar na mesma pasta para você não precisar de nenhuma configuração extra.

[06:57] Então, agora eu tenho um servidor do Selenium rodando que conhece o nosso Chrome WebDriver, e eu já tenho aqui no nosso projeto o Php-webdriver instalado e configurado.

[07:07] Então, o nosso ambiente está pronto, eu tenho tudo aqui para nós começarmos a botar a mão na massa e realmente automatizar o navegador para realizarmos testes. Então, é exatamente isso que nós vamos fazer no próximo vídeo.

### Para saber mais: Projeto
### Abrindo um navegador
### Interagindo com o navegador
### Faça como eu fiz
### O que aprendemos?
## 2. Primeiros testes
### Projeto da aula anterior
### Buscando elementos
### Classe de busca
### Buscando de outras formas
### Interagindo com o driver
### Para saber mais: Interações
### Faça como eu fiz
### O que aprendemos?
## 3. Trabalhando com formulários
### Projeto da aula anterior
### Preenchendo dados
### Submetendo forms
### Formulários
### Banco de dados
### Selecionando opções
### Elementos complexos
### Para saber mais: Campos complexos
### Faça como eu fiz
### O que aprendemos?
## 4. Otimizando recursos
### Projeto da aula anterior
### Fechando o navegador
### Extraindo setUp
### Organização
### Apenas 1 navegador
### Desafio: Singleton
### Faça como eu fiz
### O que aprendemos?
## 5. Usando PageObjects
### Projeto da aula anterior
### Alterações no HTML
### Criando um PageObject
### Propósito
### Atualizando os testes
### Para saber mais: PageObject
### Faça como eu fiz
### O que aprendemos?
## 6. Testes com AJAX
### Projeto da aula anterior
### Problema com ajax
### Esperando elementos
### Tipos de espera
### Outras ferramentas
### Para saber mais: Links
### Faça como eu fiz
### Projeto do curso
### O que aprendemos?

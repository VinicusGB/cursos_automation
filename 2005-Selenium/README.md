# Selenium com Python
---

**Professor:** Eduardo Mendes

**Disponível:** <a href="https://www.youtube.com/playlist?list=PLOQgLBuj2-3LqnMYKZZgzeC7CKCPF375B">YouTube</a>

## 0. Configurando seu ambiente Windows
### Requisitos:
- **Python:** 3.7+ (python.org)
- **Editor:** Atom (atom.io)
- **Navegadores:**
  - Firefox / Chrome
- **WebDriver:**
  - GeckoDriver
  - ChromeDriver
- **Chocolatey:** Gerenciador de pacotes do Windows
  - <a href="https://chocolatey.org/install#individual" target="_blank">Documentation</a>

## 1. O que é Selenium?
Documentação: [Selenium]("https://pypi.org/project/selenium/") | [WEBDriver]("https://github.com/rasjani/webdrivermanager") | [IDE]("https://github.com/rasjani/webdrivermanager")


- ***É uma biblioteca, de software livre, sob licença Apache 2.0, que te ajuda a resolver trabalhos manuais e repetitivos usando o browser.***
  - **biblioteca:** conjunto de ferramentas
  - **software livre:** ferramenta gratuita, colaborativa
  - **Apache 2.0:** licença que garante a sua liberdade, a burocracia dos direitos autorais

### Para que serve o Selenium

- Automação de testes de software
- Criação de bots
- Redução de trabalho 'repetitivo'
- 'Raspar' dados da internet

### História do Selenium

O projeto Selenium nasceu em 2004 com a ideia de "usar" browsers como um usuário faria.
- simples e conciso
- é compatível com a maioria dos browser
- e a recomendação da W3C (World Wide Web Consontium)

Selenium foi criado pro Jason Huggins, em 2004 para testar uma aplicação de T&E crada em PYthon e Plone.

Eles estavam tendo vários problemas por adicionar JavaScript nos projetos.
- "JavaScriptTestRunner"
  - A ferramenta se tornou livre no mesmo ano da criação

Em 2006 no Japão, Shinya Kasatani, se interessou pelo projeto e criou o Selenium-IDE.
- Uma extensão para Firefox

Em 2007 Simon Stewart, nos laboratórios da ThoughtWorks. Melhorou a maneira de interação de selenium com os navegadores.
- Assim a versão 2.0 e o Selenium WEBDriver.

Em 2008, Phillpe Hanrigou, também na ThougtWorks criou o Selenium GRID.

Depois de um tempo nasceu uma ferramenta concorrente chamada Mercury.
- O Selênio é usado para curar envenenamento por Mercúrio.

### Selenium IDE

É um plugin para o browsers que permite que você faça a sua automação "gravando" o que você faz no navegador e ele as reproduz.

Com isso é possível automatizar tarefas mesmo sem entender de programação.

### Selenium WEBDriver

Seria um interpretador do código Selenium e transferir para o navegador.
- podemos criar um código Selenium e o WEBDriver converte as ações para o navegador especificado

### Selenium GRID

Permite que utilize diversos browsers ao mesmo tempo.
- O GRID é o servidor para rodar o código em um local ideal e específico.
  - HUBS: 
  - NODES: 

## 2. Introdução ao Python

## 3. Minha primeira automação
### Entendendo o código para abrir o browser
### Teoria
#### HTML - HyperText Markup Language
##### Elementos
São tags HTML para o navegador identificar.
  
    <tag atributos=valor>
      Conteúdo
    </tag>

#### DOM - Document Object Model
Arquitetura DOM

              DOM

LOCATION  | DOCUMENT  | HISTORY

1. LOCATION
    - refresh
2. DOCUMENT
    - finds
        - text / attribute('href')
    - get
    - title
    -
3. NAVEGACION HISTORY
    - back
    - foward

## 4. Navegação e atributos
### Busca aninhada

São as buscas de tags aninhadas dentro de tags principais.

### Atributos

São as buscas por atributos de uma tag.

### Navegação

Na navegação temos o histórico de navegação da guia.
Mas os histórico não registra apenas as requisições solicitadas para o servidor ele registra as alterações dos seletores css e JavaScript.
Seria animações e ações.

## 5. Procurando e interagindo com elementos I
Documentação: [HTML]("https://html.spec.whatwg.org/multipage/") | [Mozilla]("https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes")
### Atributos
#### Globais
Atributos comuns a todas as tags do html.
#### CSS
- id: nome único para cada WEBElement
  - _find_element_by_id_
- class: nome de um grupo de WEBElement
  - _find_element_by_class_name_
- autofocus: página quando carrega faz um autofoco no elemento
- acesskey: adiciona um atalho do teclado
- title: texto para mostrar quando o mouse é posicionado em cima
- hidden: atributo para esconder a tag
- label: campo de texto
- form: tag que agrupam os elementos de inputs dos usuários:
  - name: atributo que nomeia um elemento de um formulário `<form>`
    - _find_element_by_name_
  - input: tag campo onde o usuário pode inserir dados
  - target: atributo que diz qual aba
    - self: mesma aba
    - blank: nova aba
  - action: o que fazer com a requisição
    - url
  - method: 
    - get: obter dados
    - post: enviar dados
### Interagir com o site
- send_keys: serve para adicionar texto nos formulários
  - object.send_keys('texto no campo')
- click: serve para clicar em elementos do meu form
  - object.click()

## 6. Procurando e interagindo com elemento II
### Um pouco de teoria dos seletores

Seletores são maneiras de encontrar elementos dentro de uma estrutura html (pode ser xml também) que tem uma sintaxw própria e nomenclaturas próprias.

De maneira simplória é uma maneira de selecionar elementos usando os atributos dos próprios elemtntos.

Já fizemos isso com os métodos find_element_by_[class_namme,tag_name,...]

### CSS selector
#### Básicos
- find_element_by_css_selector(selector)
  - id: ‘#id’
  - Tipo [tag]: ‘tag’
  - Classe: ‘.class’ 'tag.class'
- find_elements_by_css_selector(‘[attribute]’)
  - Atributo: '[attribute]' - '[attr op value]'
    - operador (op):
      - = (igual) / *= (ocorrer em ) / |= (exatamente ou iniciar) / ^= (iniciado com) / $= (termina com) / ~= (exatamente igual)
    - ‘[class=”form-group”]’ : Todos atributos class em que o valor seja exatamente igual a form-group
    - ‘[class*=”group”]’ : Todos atributos class em que a palavra group exista
    - ‘[type$=”t”]’ : Todos os atributos type que o final do valor seja t

#### Universal
- find_elements_by_css_selector(‘*’)

#### Combinados
- find_elementS_by_css_selector(‘input[type$=”t”]’) : Todos as tags input com atributos type que o final do valor seja t
- find_elementS_by_css_selector(‘label[for*=”n”]’) : Todos as tags label onde os atributos for contenham n
- find_elementS_by_css_selector(‘h2 ~ div’) : Encontra todas as tags div que estejam no mesmo nível de h2

#### Seletores de Grupo

- find_elementS_by_css_selector(‘label, input’) : Encontra qualquer tag label juntamente a qualquer tag type
- find_elementS_by_css_selector(‘label[for], *[type$=”t”]’) : Encontra qualquer tag label que contenha o atributo for juntamente a quaisquer tags (*) que tenham o atributo type com valor que termine em t

#### Combinadores
- Irmãos adjacentes (A + B)
  - find_elementS_by_css_selector(‘div + br’) : Encontra qualquer br após uma div
  - find_element_by_css_selector(‘h2 + div’ : Encontra a primeiro div após uma h2
- Geral de irmãos (A ~ B)
  - find_elementS_by_css_selector(‘h2 ~ div’) : Encontra todas as tags div que estejam no mesmo nível de h2
- Filhos (A > B)
  - find_elementS_by_css_selector(‘div > br’) : Encontra todas as tags br que sejam filhas de div
- Descendentes (A B)
  - find_elementS_by_css_selector(‘form br’) : Encontra todas as tags br que sejam filhas de form direta ou indiretamente

## 7-8. Eventos
### Roteiro
● DOM
● CSSOM
● Eventos
● Ouvinte de eventos
Conhecendo nosso caso nas aulas de eventos

### Conceitos
#### Vamos acessar aula 07 a
https://selenium.dunossauro.live/aula_07_a

#### Eventos
https://developer.mozilla.org/en-US/docs/Web/API/event

Eventos são super poderes que um Web Element adquirem pode ter para interagir com o usuário. É como pensar em elementos com comportamento dinâmico.

Event é uma API do browser e tem várias interfaces que herdam suas características para finalidades específicas.
Eventos
- DOM
  - Inserir elementos
  - Remover elementos
- CSSOM
  - Alterar estilo
  - Adicionar estilo
  - Salvar cookies
  - Checar conexão com a internet
  - Salvar mensagens do DB do browser
  - ….

#### API de eventos
Eventos tem duas características importantes:
- Tipo (type) [nome]
- Alvo (target)
  - bubbles, cancelable, currentTarget, defaultPrevented, timestamp, istrusted, ...

#### Mostrar lista de eventos
https://developer.mozilla.org/en-US/docs/Web/Events

- Linguagens de script
  - JavaScript
  - TypeScript
  - Elm
- Alternativas em bibliotecas Python
  - Brython *
  - Pypy.js
  - Batavia
  - Transcript

#### Juntando o que sabemos até agora
- Eventos API de eventos
  - Select
    - AddListener
    - Type Listener
    - Função Evento escolhido
  - Inline
    - HTML
    - Atributo type
    - Função
#### Vamos acessar aula 07 b
https://selenium.dunossauro.live/aula_07_b
#### Vamos acessar aula 07 c
https://selenium.dunossauro.live/aula_07_c
Trabalhando com eventos
#### Os eventos que vamos estudar
- Foco (focus)
- Mudança (change)
- Mouse
- Drag
- Teclado
https://developer.mozilla.org/en-US/docs/Web/Events

#### Focus x Blur
Evento de foco. Quando o elemento é “acessado” ele está em foco. Com isso o evento “Focus” é disparado.
Quando o elemento perde o foco, o evento Blur é desencadeado
https://selenium.dunossauro.live/aula_07_d

#### Vamos codar um tikin
https://selenium.dunossauro.live/aula_07_d

### Eventos + Selenium | Parte 1 | Observando os eventos
A biblioteca do selenium conta com um mecanismo para observar eventos. Um EventListener [Escutador de eventos]. A implementação dele é baseada em um padrão de projeto chamado Template Method.
A ideia principal é fazer uma ação “antes” e/ou “depois” de alguma determinada ação do WebDriver

#### Observando os eventos
“Antes” e “Depois”, geralmente são conhecidos como Hooks.
Vamos usar o método ‘click’, como exemplo.
WE <- click -> WE
Estado anterior ao click <- -> Estado posterior ao click
#### EventListener
https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.abstract_event_listener

O objetivo do EventListener é observar o estado do WD em todos os momentos. 
Antes e depois de uma ação ser executada.
Por exemplo, todas as vezes em que o ‘click’ for chamado podemos observar o estado do dom, de um único elemento, fazer logs, etc...

WE <- click -> WE

.before_click() <- .click() -> .after_click()

- Uma breve olhada (AbstractEventListener)
  - Navegação
    - .navigate_back
    - .navigate_forward
    - .navigate_to
  - Seletores
    - .find
  - Ações
    - .click
    - .change_value_of
    - .execute_script

#### Vamos codar um tikin aula 07 d
https://selenium.dunossauro.live/aula_07_d

#### Event Firing
Disparador de eventos

O disparador de eventos é uma “burocracia” do selenium para usar um Listener.
Ele constrói um wrapper do webdriver e dispara os eventos para o Listener.

#### Exercício 7
https://selenium.dunossauro.live/exercicio_07

Refazer:
https://selenium.dunossauro.live/exercicio_03
* usar o EventListener para printar a o after de 
navegação e de clicks
- Lições para casa:
  - Assistir a Live de Python #61 - Introdução a orientação a objetos
    - Se lidar com classes for um problema para você
  - Assistir a Live de Python #68 - Interfaces de ABCs
    - Se quiser entender o que é abstrato
  - Assistir a Live de Python #115 - Introdução aos padrões de projeto
    - Vamos usar esse conceitos na aula de page objects
  - Assistir a Live de Python #117 - Padrão template method
    - Se quiser entender como funciona o AbstractEventListener


### Eventos + Selenium | Parte 2 | Interagindo com os eventos

Eventos, em grande maioria, dependem de interações do usuário.
Nós podemos interagir com o browser de várias maneiras:
- Mouse
- Teclado
- Touch*
- ...
#### Selenium [https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement]
- webdriver.webelement
  - Atributos
    - .text
    - .tag_name
  - Seletores
    - .find_element
  - Consulta
    - .get_attribute
    - .is_displayed
  - Ações
    - .click
    - .send_keys

- Ações
  - Mouse
    - .click
  - Teclado
    - .send_keys
    - .submit
    - .clear
  - Screenshot
    - .screenshot
    - .as_base64
    - .as_png

Cadeias de ações [https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains]

Por exemplo, como uma tecla é pressionada?
- key Down
- key Up

##### Hi-level
- Descrevendo ações:
  - nome = browser.find_element(by.ID,'nome')
  - nome.send_keys('eduardo')

##### Low-level
- Descrevendo ações:
  - nome = browser.find_element(by.ID, ‘nome’)
    - move_to_element(nome)
    - key_down(‘e’)
    - key_up(‘e’)
    - key_down(‘d’)
    - key_up(‘d’)
    - key_down(‘u’)



#### TECLADO - Keyboard Events
https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent

##### Eventos de teclado
- Existem 3* tipos de eventos disparados por teclado
  - keyup
  - keydown
  - accesskey
  - keypress (obsoleto)
_Normal keyDown keyDown_

##### Atributos de teclado
E também temos vários atributos, dos quais vou destacar 3 que considero mais importantes
- key (Valor da tecla)
- Atributos de teclas
  - shiftKey
  - altKey
  - metaKey
  - ctrlKey
- getModifierState()
  - CapsLock
  - shift
  - meta
  - os

##### Vamos testar + Codar
https://selenium.dunossauro.live/keyboard

##### Action Chains
Action Chains são maneiras de automatizar ações de baixo nível.

- ActionChains
  - Teclado
    - .key_down
    - .key_up
    - .send_keys
    - .send_keys_to_element
- Movimento
    - .move_by_offset
    - .move_to_element
    - .move_to_element_with_offset

##### O fluxo
- AC
  - .perform() -> [.move_to_element .key_down .key_up]
  - 
- WD
  - .find_element

##### Keys
https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.keys

##### O fluxo
- AC
  - .perform() -. [.move_to_element KEYS [.key_down .key_up]]
- WD
  - .find_element

Vamos tentar de novo
https://selenium.dunossauro.live/aula_08_a

#### Voltando ao início - aula 08 a
https://selenium.dunossauro.live/aula_08_a

#### MOUSE
Relembrar é viver
https://selenium.dunossauro.live/caixinha
Selenium [https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement]
##### Action Chains

- ActionChains
  - Teclado
    - .key_down
    - .key_up
    - .send_keys
    - .send_keys_to_element
  - Movimento
    - .move_by_offset
    - .move_to_element
    - .move_to_element_with_offset
  - Mouse
    - .click
    - .click_and_hold
    - .context_click
    - .double_click

##### Eventos de Mouse
Tipos de eventos disparados por teclado
- .move_to_element (disparados por teclado)
  - mouseenter
  - mouseleave]
- click
- dblclick
- contextmenu

##### Atributos de ação
- shiftKey
- altKey
- metaKey
- ctrlKey

##### Agora vai
https://selenium.dunossauro.live/caixinha

#### DRAG and DROP (DnD)
https://github.com/SeleniumHQ/selenium/issues/8345

#### Exercício 8
https://selenium.dunossauro.live/caixinha
● Dizer todas as cores possíveis da caixinha
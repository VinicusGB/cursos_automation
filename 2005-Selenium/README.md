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

## 5. Procurando e interagindo com elementos
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

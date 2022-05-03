from selenium.webdriver import Firefox

browser = Firefox()

url = 'https://curso-python-selenium.netlify.app/aula_04_a.html'
browser.get(url)

def find_by_text(browser,tag,text):
    """ Encontrar o elemento com o texto 'text'.
        Arguments:
        - browser = Instância do browsser [firefox, chrome, safari, ...]
        - texto = Conteúdo que deve estar na tag
        - tag = onde o texto deve ser procurado
    """
    elements = browser.find_elements_by_tag_name(tag)

    for element in elements:
        if element.text == text:
            return element
        

elemento_dog = find_by_text(browser,'li','DuckDuckGo')

def find_by_href(browser,link):
    """ Encontrar o elemento 'a' com o link 'href'.
        Arguments:
        - browser = Instância do browsser [firefox, chrome, safari, ...]
        - link = link que será procurado em todas as tags 'a'
    """
    elements = browser.find_elements_by_tag_name('a')

    for element in elements:
        if link in element.get_attribute('href'):
            return element


elemento_ddg = find_by_href(browser,'ddg')

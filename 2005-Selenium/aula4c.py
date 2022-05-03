from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()

url = 'https://curso-python-selenium.netlify.app/aula_04_b.html'
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

sleep(3)

nome_das_caixas = ['um','dois','tres','quatro']

for text in nome_das_caixas:
    find_by_text(browser,'div',text).click()

for text in nome_das_caixas:
    browser.back()
    sleep(0.2)

for text in nome_das_caixas:
    browser.forward()
    sleep(0.2)

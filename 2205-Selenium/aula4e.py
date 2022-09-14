from selenium.webdriver import Firefox
from urllib.parse import urlparse
from time import sleep
from pprint import pprint

browser = Firefox()

url = 'https://curso-python-selenium.netlify.app/aula_04.html'
browser.get(url)

sleep(2)

url_atual = urlparse(browser.current_url)

aside = browser.find_element_by_tag_name('aside')

aside_ancoras = aside.find_elements_by_tag_name('a')

resultado_1 = {}

for ancora in aside_ancoras:
    resultado_1[ancora.text] = ancora.get_attribute('href')

pprint(resultado_1)

browser.get(resultado_1['Aula 3'])

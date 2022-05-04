from calendar import day_abbr, month
from selenium.webdriver import Firefox
from time import sleep
from datetime import date

def search_pgr():
    for elemento in search_pg:
        if 'ctl00_cphConteudo_txtPalavraChave' in elemento.get_attribute('id'):
            elemento.send_keys('Relação de licença médica')

dt_now = date.today()
d = date.day
m = date.month
y = date.y

browser = Firefox()

url = "http://www.docidadesp.imprensaoficial.com.br/Busca.aspx"
browser.get(url)

sleep(3)


search_im = browser.find_element_by_id('ctl00_cphConteudo_txtPalavraChave')
search_bt = browser.find_element_by_id('ctl00_cphConteudo_ibtsearch_bt')

search_in.send_keys('Relação de licença médica')
search_bt.click()

sleep(3)


select = browser.find_elements_by_class_name('lnkModifier')

for s
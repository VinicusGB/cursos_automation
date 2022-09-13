from calendar import day_abbr, month
from selenium.webdriver import Firefox
from time import sleep
from datetime import date

def search_pgr(lista):
    for elemento in lista:
        if 'ctl00_cphConteudo_txtPalavraChave' in elemento.get_attribute('id'):
            elemento.send_keys('Relação de licença médica')

def search_moth(m):
    month_list = {
        1 : 'Janeiro',
        2 : 'Fevereiro',
        3 : 'Março',
        4 : 'Abril',
        5 : 'Maio',
        6 : 'Junho',
        7 : 'Julho',
        8 : 'Agosto',
        9 : 'Setembro',
        10 : 'Outubro',
        11 : 'Novembro',
        12 : 'Dezembro'
        }
    return month_list[m]


dt_now = date.today()
d = str(dt_now.day)
m = search_moth(dt_now.month) 
y = str(dt_now.year)

browser = Firefox()
browser.maximize_window()

url = "http://www.docidadesp.imprensaoficial.com.br/BuscaAvancada.aspx"
browser.get(url)
print('\n####\nAbrindo a páginas\n####\n')

sleep(3)


#search_in = browser.find_element_by_id('ctl00_cphConteudo_txtPalavraChave')
search_in = browser.find_element(by='id',value='ctl00_cphConteudo_txtPalavraChave')

#search_bt = browser.find_element_by_id('ctl00_cphConteudo_ibtBuscar_bt')
#search_bt = browser.find_element(by='id',value='ctl00_cphConteudo_ibtBuscar')

print('\n####\nRealizando a pesquisa\n####\n')
search_in.send_keys('Relação de licença médica')
browser.find_element(by='id',value='ctl00_cphConteudo_ibtBuscar').click()
print('\n####\nCliando em buscar\n####\n')

sleep(3)

print('\n####\nfiltrando por data\n####\n')
browser.find_element_by_partial_link_text(y).click()
sleep(0.5)
browser.find_element_by_partial_link_text(m).click()
sleep(0.5)
browser.find_element_by_partial_link_text(d).click()
sleep(0.5)
browser.find_element(by='id',value='ctl00_cphConteudo_GridResultados1_rptEdicoes_ctl01_hlAbrePDF').click()
sleep(5)

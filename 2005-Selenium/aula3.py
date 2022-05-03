from selenium.webdriver import Firefox
#from selenium.webdriver import Chrome

# Abre o navegador
navegador = Firefox()
#navegador = Chrome()

# Acessar uma página
url = 'https://curso-python-selenium.netlify.app/aula_03.html'
navegador.get(url)

# Aguaradar carregar a página
from time import sleep
sleep(5)

# Procurando elementos no HTML
a = navegador.find_element_by_tag_name('a')
ass = navegador.find_elements_by_tag_name('a')
p = navegador.find_element_by_tag_name('p')

# Clicar no elemento
#meu_p.click()

for click in range(10):
    ps = navegador.find_elements_by_tag_name('p')
    a.click()
    print(f'Valor do ultimo p: {ps[-1].text} valor do click: {click}')

    print(f'Os valores são iguais {ps[-1].text == str(click)}')

# Encerra o navegador
#navegador.quit()

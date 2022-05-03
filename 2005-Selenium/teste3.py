from selenium.webdriver import Firefox

# Abre o navegador
navegador = Firefox()

# Acessar uma página
url = 'https://piunivespjacana.herokuapp.com/abrigo/parceiros'
navegador.get(url)

# Aguaradar carregar a página
from time import sleep
sleep(5)

# Procurando elementos no HTML
a = navegador.find_element_by_tag_name('a')
ass = navegador.find_elements_by_tag_name('a')
p = navegador.find_element_by_tag_name('p')

# Clicar no elemento

for i in ass:
    print(i.text)
    if i.text == 'Confira aqui!':
        i.click()

# Encerra o navegador
#navegador.quit()

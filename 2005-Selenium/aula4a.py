from selenium.webdriver import Firefox

url = 'https://curso-python-selenium.netlify.app/aula_04_a.html'

browser = Firefox()

browser.get(url)

"""
1. find 'ul'
2. find all 'li'
3. In (1), find 'a' and get your text
===
4. result: lista_n_ordenada[-1][0].text
"""
lista_n_ordenada = browser.find_elements_by_tag_name('ul')  #1
lis = lista_n_ordenada.find_elements_by_tab_name('li')      #2
lis[0].find_element_by_tag_name('a').text                   #3
print("resumo".lista_n_ordenada[-1][0].text)                        

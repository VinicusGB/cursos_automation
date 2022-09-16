from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


browser = browser = Firefox(executable_path=r'C:\Projetos\tools\selenium_geckodriver\firefox\geckodriver.exe')
browser.maximize_window()

#browser.get('http://www.google.com')
browser.get('https://elos-be.herokuapp.com/elos/')
sleep(.5)

parceiros = browser.find_element_by_xpath('/html/body/header/nav/div/div/ul[1]/li[2]/a')
parceiros.click()
sleep(.5)
eventos = browser.find_element_by_xpath('/html/body/header/nav/div/div/ul[1]/li[3]/a')
eventos.click()
sleep(.5)
blog = browser.find_element_by_xpath('/html/body/header/nav/div/div/ul[1]/li[4]/a')
blog.click()
sleep(.5)
elos = browser.find_element_by_xpath('/html/body/header/nav/div/div/ul[1]/li[1]/a')
elos.click()
sleep(.5)
'''menu = browser.find_element_by_xpath('/html/body/header/nav/div/div/ul[2]/li/div/a[2]')
menu.click()
sleep(1)
inscreva = browser.find_element_by_xpath('/html/body/header/nav/div/div/ul[2]/li/div/a[2]')
inscreva.click()'''
browser.get('http://elos-be.herokuapp.com/via_cep')
sleep(1)
via_cep = browser.find_element_by_xpath('//*[@id="cep"]')
sleep(1)
via_cep.send_keys('02460030')
sleep(2)
consulta = browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/form/div/div[2]/button')
consulta.click()
via_cep = browser.find_element_by_xpath('//*[@id="cep"]')
sleep(2)
via_cep.send_keys('50050030')
sleep(2)
consulta = browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/form/div/div[2]/button')
consulta.click()
sleep(5)

usuario = browser.find_element(By.XPATH,'//*[@id="id_username"]')
usuario.send_keys('teste')
email = browser.find_element(By.XPATH,'//*[@id="id_email"]')
email.send_keys('teste')
senha = browser.find_element(By.XPATH,'//*[@id="id_password1"]')
senha.send_keys('teste')
conf_senha = browser.find_element(By.XPATH,'//*[@id="id_password2"]')
conf_senha.send_keys('teste')
buton = browser.find_element(By.XPATH,'/html/body/main[1]/div/div/div/form/button')
buton.click()
sleep(5)

#browser.quit()

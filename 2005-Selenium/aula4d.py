from selenium.webdriver import Firefox
from urllib.parse import urlparse

browser = Firefox()

url = 'https://curso-python-selenium.netlify.app/aula_04_b.html'
browser.get(url)

url_atual = urlparse(browser.current_url)

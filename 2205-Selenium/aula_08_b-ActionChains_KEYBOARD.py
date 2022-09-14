from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import (
    ActionChains
)
from selenium.webdriver.common.keys import Keys

url = 'https://selenium.dunossauro.live/aula_08_a'
texto = 'Selenium'

browser = Firefox()
browser.get(url)

# hi-level
elemento = browser.find_element_by_name('texto')

# low-level
ac = ActionChains(browser)      # Ativa o modo low-level
ac.move_to_element(elemento)    # Necessário mover para o elemento
ac.click(elemento)              # Clica no elemento para ficar em foco


def digita_com(key):
    ac.key_down(key)        # Pressiona a tecla
    for letra in texto:
        ac.key_down(letra)
        ac.key_up(letra)
    ac.key_up(key)          # Despressiona a tecla

digita_com(Keys.SHIFT)
digita_com(Keys.CAPS)

# Todo o procedimento acima só executa após mandar o perfomance
ac.perform()

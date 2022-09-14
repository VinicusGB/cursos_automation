from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

url = 'https://selenium.dunossauro.live/aula_08_a'
texto = 'Selenium'

browser = Firefox()
browser.get(url)

# low-level
ac = ActionChains(browser)      # Ativa o modo low-level

# Métodos do ActionChains
## click                            | botão de click do mouse
## click_and_hold                   | clica e segura
## context_click                    | botão de contexto do mouse
## double_click                     | duplo clique do mouse
## drag_and_drop                    | arrasta e solta
## drag_and_drop_by_offset          | arrasta e solta no percurso
## key_down                         | pressiona uma tecla
## key_up                           | despressiona uma tecla
## move_by_offset                   | mover no percurso
## move_to_element                  | mover para o elemento
## move_to_element_with_offset      | mover para o elemento durante o percurso
## pause                            | espera
## perform                          | EXECUTA OS PARÂMETROS
## release                          | soltar
## reset_actions                    | limpa uma ação
## scroll                           | scroll
## send_keys                        | digita
## send_keys_to_element             | digita no elemento
## w3c_actions

# Keys

## ALT
## CONTROL
## SHIFT
## TAB
## LEFT_ALT
## LEFT_CONTROL
## LEFT_SHIFT

## ENTER
## BACKSPACE
## BACK_SPACE
## ESCAPE
## SPACE
## CANCEL
## CLEAR
## COMMAND

## ARROW_DOWN
## ARROW_LEFT
## ARROW_RIGHT
## ARROW_UP

## INSERT
## DELETE
## HOME
## END
## PAGE_UP
## PAGE_DOWN

## UP
## DOWN
## LEFT
## RIGHT

## ADD
## SUBTRACT
## DIVIDE
## EQUALS

## DECIMAL
## SEMICOLON
## SEPARATOR

## F1
## F2
## F3
## F4
## F5
## F6
## F7
## F8
## F9
## F10
## F11
## F12

## NUMPAD0
## NUMPAD1
## NUMPAD2
## NUMPAD3
## NUMPAD4
## NUMPAD5
## NUMPAD6
## NUMPAD7
## NUMPAD8
## NUMPAD9

## HELP

## META
## MULTIPLY
## NULL
## PAUSE
## RETURN

## ZENKAKU_HANKAKU

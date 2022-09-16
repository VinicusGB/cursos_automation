from selenium.webdriver import Firefox
from pages.pages import PageTodo

browser = Firefox()

pagina = PageTodo(
    browser,
    'http://selenium.dunossauro.live/todo_list.html'
)

pagina.open()
pagina.todo.create_todo(
    'POM','POM POM POMMMMMMMMMMM'
)

# AAA - 31

'''
- ARRANGE = ORGANIZAR/ARRUMAR
- ACT = AGIR
- ASSERT = AFIRMAR/GARANTIR
'''


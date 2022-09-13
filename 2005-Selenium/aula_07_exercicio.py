from selenium.webdriver import Firefox
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver

class Monitora(AbstractEventListener):
    def after_change_value_of(self, element, driver):
        '''after_change_value_of:
        Evento sobre o elemento após alterar o valor'''
        return super().after_change_value_of(element, driver)
    def after_click(self, element, driver):
        '''after_click:
        Evento sobre o elemento após o clique'''
        return super().after_click(element, driver)
    def after_close(self, driver):
        '''after_close:
        Evento sobre o driver(navegador) após encerrar a instância do objeto'''
        return super().after_close(driver)
    # after_execute_script
    def after_execute_script(self, script, driver):
        return super().after_execute_script(script, driver)
    def after_find(self, by, value, driver):
        '''after_find:
        Evento sobre o elemento após localizar o elemento'''
        return super().after_find(by, value, driver)
    def after_navigate_back(self, driver):
        '''after_navigate_back:
        Evento sobre o driver(navegador) após voltar para a página anterior'''
        return super().after_navigate_back(driver)
    def after_navigate_forward(self, driver):
        '''after_navigate)foward: 
        Evento sobro o driver(navegador) após avançar para a próxima página'''
        return super().after_navigate_forward(driver)
    def after_navigate_to(self, url, driver):
        '''after_navigate_to:
        Evento sobre o driver(navegador) após carregar a página'''
        return super().after_navigate_to(url, driver)
    def after_quit(self, driver):
        '''after_quit: 
        Método sobre o driver(navegador) após fechar/encerrar o navegador'''
        return super().after_quit(driver)
    def before_change_value_of(self, element, driver):
        '''before_change_value_of: 
        Evento sobre o elemento antes de alterar o valor'''
        return super().before_change_value_of(element, driver)
    def before_click(self, element, driver):
        '''before_click: 
        Evento sobre o elemento antes do click'''
        return super().before_click(element, driver)
    def before_close(self, driver):
        '''# before_close: 
        Evento sobre o driver(navegador) antes de encerrar a instância do objeto'''
        return super().before_close(driver)
    # before_execute_script
    def before_execute_script(self, script, driver):
        '''
        Evento sobre o driver(navagador) antes de executar o script'''
        return super().before_execute_script(script, driver)
    def before_find(self, by, value, driver):
        '''# before_find: 
        Evento sobre o elemento antes de localizar'''
        return super().before_find(by, value, driver)
    # before_navigate_back
    def before_navigate_back(self, driver):
        '''
        Evento sobre o driver(navegador) antes de voltar para a página anterior'''
        return super().before_navigate_back(driver)
    # before_navigate_forward
    def before_navigate_forward(self, driver):
        '''
        Evento sobre o driver(navegador) antes de navegara para a próxima página'''
        return super().before_navigate_forward(driver)
    # before_navigate_to
    def before_navigate_to(self, url, driver):
        '''
        Evento sobre o driver(navegador) antes de ir para uma nova url'''
        return super().before_navigate_to(url, driver)
    # before_quit
    def before_quit(self, driver):
        '''
        Evento sobre o driver(navegador) antes de encerrar/fechar o navagador'''
        return super().before_quit(driver)
    # on_exception
    def on_exception(self, exception, driver):
        '''
        Evento sobre o driver(navegador) caso ocorra um exceção'''
        return super().on_exception(exception, driver)

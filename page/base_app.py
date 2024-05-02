from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseApp:
    '''Базовый класс работы с андроидом'''

    def __init__(self, app):
        self.app = app

    def find(self, args):
        '''Поиск элемента'''

        return self.app.find_element(*args)

    def wait(self, args):
        '''Ожидание видимого элемента'''

        WebDriverWait(self.app, 10).until(EC.presence_of_element_located(args))

    def wait_click(self, args):
        '''Ожидание кликабельного элемента'''

        WebDriverWait(self.app, 10).until(EC.element_to_be_clickable(args))

    def sms(self):
        '''Ввод смс подтверждения'''

        self.app.press_keycode(7)
        self.app.press_keycode(7)
        self.app.press_keycode(7)
        self.app.press_keycode(8)

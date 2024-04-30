from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseApp:
    '''Базовый класс работы с андроидом'''

    def __init__(self, app):
        self.app = app

    def find(self, args):
        '''Ожидаем и находим нужный элемент'''
        WebDriverWait(self.app, 10).until(
            EC.presence_of_element_located(
                args)
        )
        self.app.find_element(*args)

    def sms(self):
        '''Ввод смс подтверждения'''
        self.app.press_keycode(7)
        self.app.press_keycode(7)
        self.app.press_keycode(7)
        self.app.press_keycode(8)

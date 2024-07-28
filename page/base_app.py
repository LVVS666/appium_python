from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseApp:
    '''Базовый класс работы с андроидом'''

    def __init__(self, app):
        self.app = app

    def find(self, args):
        '''Поиск элемента'''
        return self.app.find_element(*args)

    def wait(self, args):
        '''Ожидание видимого элемента'''
        WebDriverWait(self.app, 20).until(EC.presence_of_element_located(args))

    def wait_not(self, args):
        '''Ожидание невидимого элемента'''
        WebDriverWait(self.app, 5).until(EC.presence_of_element_located(args))

    def wait_banner_and_push(self, args):
        '''Ожидание баннера или уведомления'''
        WebDriverWait(self.app, 10).until(EC.presence_of_element_located(args))

    def click_element(self, locator):
        '''Кликнуть по элементу'''
        self.wait_click(locator)
        locator_element = self.find(locator)
        locator_element.click()

    def send_keys_element(self, locator, text):
        '''Заполнить форму элемента текстом'''
        self.wait(locator)
        locator_element = self.find(locator)
        locator_element.click()
        locator_element.send_keys(text)

    def send_keys_element_click(self, locator, text):
        '''Заполнить форму элемента текстом'''
        self.wait(locator)
        locator_element = self.find(locator)
        locator_element.send_keys(text)
        locator_element.click()

    def wait_click(self, args):
        '''Ожидание кликабельного элемента'''
        WebDriverWait(self.app, 20).until(EC.element_to_be_clickable(args))


    def sms(self):
        '''Ввод смс подтверждения'''
        self.app.press_keycode(7)
        self.app.press_keycode(7)
        self.app.press_keycode(7)
        self.app.press_keycode(8)

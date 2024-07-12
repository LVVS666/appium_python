from selenium.common import TimeoutException
from element_locators import auth_elements as el_auth
from page.base_app import BaseApp

class Auth(BaseApp):
    '''Класс авторизации пользователя'''
    def auth(self, code_phone, phone):
        '''Авторизация пользователя через телефон'''
        self.click_element(el_auth.login_in_phone)
        self.click_element(el_auth.code_country)
        if code_phone == el_auth.kirgistan_code:
            self.send_keys_element(el_auth.search_country, 'Киргизия')
        self.click_element(code_phone)
        self.send_keys_element(el_auth.form_phone, phone)
        self.click_element(el_auth.button_send_phone)
        self.click_element(el_auth.code_input)
        self.sms()
        # добавить ожидание плашки с картами
        # закрыть плашку

    def registration(self, code_phone, country, phone):
        '''Регистрация пользователя через телефон'''
        self.click_element(el_auth.login_in_phone)
        self.click_element(el_auth.code_country)
        if code_phone == el_auth.kirgistan_code:
            self.send_keys_element(el_auth.search_country, 'Киргизия')
        self.click_element(code_phone)
        self.send_keys_element(el_auth.form_phone, phone)
        self.click_element(el_auth.button_send_phone)
        self.click_element(el_auth.code_input)
        self.sms()
        self.click_element(country)
        self.click_element(el_auth.button_send_country)
        # добавить ожидание плашки с картами
        # закрыть плашку

    def delete_user(self):
        '''Удаление активного пользователя'''
        self.click_element(el_auth.main_menu)
        self.click_element(el_auth.profile_user)
        self.click_element(el_auth.exit_and_delete)
        self.click_element(el_auth.delete_user)
        self.click_element(el_auth.on_delete)
        self.click_element(el_auth.complete_delete_button)


    def button_sub(self):
        '''Проверка кнопки подписки на карте'''
        self.wait(el_auth.subscription)
        assert self.find(el_auth.subscription), 'Кнопка подписки не найдена'

    def not_button_sub(self):
        '''Проверка отсутствия кнопки подписки на карте'''
        try:
            self.wait_not(el_auth.subscription)
            assert self.find(el_auth.subscription) is None, 'Кнопка подписки найдена'
        except TimeoutException:
            return True

    def button_bon(self):
        '''Проверка кнопки бонусов на карте'''
        self.wait(el_auth.bonuse)
        assert self.find(el_auth.bonuse), 'Кнопка бонусов не найдена'

    def not_button_bon(self):
        '''Проверка отсутствия кнопки бонусов на карте'''
        try:
            self.wait_not(el_auth.bonuse)
            assert self.find(el_auth.bonuse) is None, 'Кнопка бонусов найдена'
        except TimeoutException:
            return True

    def exit(self):
        '''Выход из аккаунта'''
        self.click_element(el_auth.main_menu)
        self.click_element(el_auth.profile_user)
        self.click_element(el_auth.exit_and_delete)
        self.click_element(el_auth.button_exit)
from element_locators import auth_elements as el
from page.base_app import BaseApp


class LoginApp(BaseApp):
    '''Класс авторизации пользователя'''

    def auth(self, code_phone, country, phone):
        '''Авторизация пользователя через телефон'''
        self.wait_click(el.login_in_phone)
        method_start = self.find(el.login_in_phone)
        method_start.click()
        self.wait_click(el.code_country)
        on_country_code = self.find(el.code_country)
        on_country_code.click()
        self.wait_click(code_phone)
        on_russian_code = self.find(code_phone)
        on_russian_code.click()
        self.wait(el.form_phone)
        send_phone = self.find(el.form_phone)
        send_phone.send_keys(phone)
        button_send_phone = self.find(el.button_send_phone)
        button_send_phone.click()
        self.wait_click(el.code_input)
        input_code = self.find(el.code_input)
        input_code.click()
        self.sms()
        self.wait_click(country)
        on_country = self.find(country)
        on_country.click()
        button_send_country = self.find(el.button_send_country)
        button_send_country.click()
        self.wait(el.main_map)

    def delete_user(self):
        '''Удаление активного пользователя'''
        menu = self.find(el.main_menu)
        menu.click()
        self.wait_click(el.profile_user)
        profile = self.find(el.profile_user)
        profile.click()
        self.wait_click(el.exit_and_delete)
        exit_delete = self.find(el.exit_and_delete)
        exit_delete.click()
        self.wait_click(el.delete_user)
        delete_button = self.find(el.delete_user)
        delete_button.click()
        self.wait_click(el.on_delete)
        delete = self.find(el.on_delete)
        delete.click()

from page.base_app import BaseApp
from element_locators import auth_elements as el


class LoginApp(BaseApp):

    def auth(self, russian_code, phone):
        self.wait(el.login_in_phone)
        method_start = self.find(el.login_in_phone)
        method_start.click()
        self.wait(el.code_country)
        on_country_code = self.find(el.code_country)
        on_country_code.click()
        self.wait(russian_code)
        on_russian_code = self.find(*russian_code)
        on_russian_code.click()
        self.wait(el.form_phone)
        send_phone = self.find(el.form_phone)
        send_phone.send_keys(phone)
        button_send_phone = self.find(el.button_send_phone)
        button_send_phone.click()
        self.wait(el.code_input)
        input_code = self.find(el.code_input)
        input_code.click()
        self.sms()

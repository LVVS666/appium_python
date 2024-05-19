import time

from element_locators import auth_elements as el_auth, doc_elements as el_doc
from page.base_app import BaseApp


class AndroidApp(BaseApp):
    '''Класс Андроид устройства'''

    def auth(self, code_phone, phone):
        '''Авторизация пользователя через телефон'''
        self.wait_click(el_auth.login_in_phone)
        method_start = self.find(el_auth.login_in_phone)
        method_start.click()
        self.wait_click(el_auth.code_country)
        on_country_code = self.find(el_auth.code_country)
        on_country_code.click()
        if code_phone == el_auth.kirgistan_code:
            self.wait(el_auth.search_country)
            send_country = self.find(el_auth.search_country)
            send_country.click()
            send_country.send_keys('Киргизия')
        self.wait_click(code_phone)
        on_russian_code = self.find(code_phone)
        on_russian_code.click()
        self.wait(el_auth.form_phone)
        send_phone = self.find(el_auth.form_phone)
        send_phone.send_keys(phone)
        button_send_phone = self.find(el_auth.button_send_phone)
        button_send_phone.click()
        self.wait_click(el_auth.code_input)
        input_code = self.find(el_auth.code_input)
        input_code.click()
        self.sms()
        self.wait(el_auth.main_map)

    def registration(self, code_phone, country, phone):
        '''Регистрация пользователя через телефон'''
        self.wait_click(el_auth.login_in_phone)
        method_start = self.find(el_auth.login_in_phone)
        method_start.click()
        self.wait_click(el_auth.code_country)
        on_country_code = self.find(el_auth.code_country)
        on_country_code.click()
        if code_phone == el_auth.kirgistan_code:
            self.wait(el_auth.search_country)
            send_country = self.find(el_auth.search_country)
            send_country.click()
            send_country.send_keys('Киргизия')
        self.wait_click(code_phone)
        on_russian_code = self.find(code_phone)
        on_russian_code.click()
        self.wait(el_auth.form_phone)
        send_phone = self.find(el_auth.form_phone)
        send_phone.send_keys(phone)
        button_send_phone = self.find(el_auth.button_send_phone)
        button_send_phone.click()
        self.wait_click(el_auth.code_input)
        input_code = self.find(el_auth.code_input)
        input_code.click()
        self.sms()
        self.wait_click(country)
        on_country = self.find(country)
        on_country.click()
        time.sleep(2)
        button_send_country = self.find(el_auth.button_send_country)
        button_send_country.click()
        self.wait(el_auth.main_map)

    def delete_user(self):
        '''Удаление активного пользователя'''
        menu = self.find(el_auth.main_menu)
        menu.click()
        self.wait_click(el_auth.profile_user)
        profile = self.find(el_auth.profile_user)
        profile.click()
        self.wait_click(el_auth.exit_and_delete)
        exit_delete = self.find(el_auth.exit_and_delete)
        exit_delete.click()
        self.wait_click(el_auth.delete_user)
        delete_button = self.find(el_auth.delete_user)
        delete_button.click()
        self.wait_click(el_auth.on_delete)
        delete = self.find(el_auth.on_delete)
        delete.click()

    def button_sub(self):
        '''Проверка кнопки подписки на карте'''
        self.wait(el_auth.subscription)
        assert self.find(el_auth.subscription), 'Кнопка подписки не найдена'

    def button_bon(self):
        '''Проверка кнопки бонусов на карте'''
        self.wait(el_auth.bonuse)
        assert self.find(el_auth.bonuse), 'Кнопка бонусов не найдена'

    def exit(self):
        '''Выход из аккаунта'''
        menu = self.find(el_auth.main_menu)
        menu.click()
        self.wait_click(el_auth.profile_user)
        profile = self.find(el_auth.profile_user)
        profile.click()
        self.wait_click(el_auth.exit_and_delete)
        exit_delete = self.find(el_auth.exit_and_delete)
        exit_delete.click()
        self.wait(el_auth.button_exit)
        bt_exit = self.find(el_auth.button_exit)
        bt_exit.click()

    def documents(self):
        '''Проверка наличия всех стран в документах'''
        menu = self.find(el_auth.main_menu)
        menu.click()
        self.wait(el_doc.documents)
        documents = self.find(el_doc.documents)
        documents.click()
        self.wait(el_doc.russian_documents)
        assert self.find(el_doc.russian_documents),'В документах отсутствует раздел Российской Федерации'
        assert self.find(el_doc.kazahstan_documents), 'В документах отсутствует раздел Казахстана'
        assert self.find(el_doc.kirgistan_documents), 'В документах отсутствует раздел Кыргызстан'
        assert self.find(el_doc.belarussia_documents), 'В документах отсутствует раздел Беларуссии'
        back = self.find(el_doc.button_back_documents)
        back.click()
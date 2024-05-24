import time

from selenium.common import TimeoutException

from element_locators import auth_elements as el_auth, doc_elements as el_doc, tariff_elements as el_tariff
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
        self.wait(el_auth.main_menu)
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

    def not_button_sub(self):
        '''Проверка отсутствия кнопки подписки на карте'''
        try:
            self.wait(el_auth.subscription)
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
            self.wait(el_auth.bonuse)
            assert self.find(el_auth.bonuse) is None, 'Кнопка бонусов найдена'
        except TimeoutException:
            return True

    def exit(self):
        '''Выход из аккаунта'''
        self.wait(el_auth.main_menu)
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
        self.wait(el_auth.outside_map)
        map = self.find(el_auth.outside_map)
        map.click()
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

    def documents_in_country(
                             self,
                             user_consent,
                             consent_text,
                             assert_consent,
                             politice_date,
                             politice_text,
                             assert_politice,
                             requisites,
                             requisites_text,
                             assert_requisites
                            ):
        '''Проверка документов у стран'''
        self.wait(el_auth.outside_map)
        map = self.find(el_auth.outside_map)
        map.click()
        menu = self.find(el_auth.main_menu)
        menu.click()
        self.wait(el_doc.documents)
        documents = self.find(el_doc.documents)
        documents.click()
        self.wait(user_consent)
        consent = self.find(user_consent)
        consent.click()
        self.wait(consent_text)
        assert_consent_text = self.find(consent_text).text
        assert assert_consent_text == assert_consent, 'Текст из <Пользовательского соглашения> не соответствует'
        button_close = self.find(el_doc.button_close)
        button_close.click()
        self.wait(el_auth.outside_map)
        map = self.find(el_auth.outside_map)
        map.click()
        self.wait(el_auth.main_menu)
        menu = self.find(el_auth.main_menu)
        menu.click()
        self.wait(el_doc.documents)
        documents = self.find(el_doc.documents)
        documents.click()
        self.wait(politice_date)
        consent = self.find(politice_date)
        consent.click()
        self.wait(politice_text)
        assert_politice_text = self.find(politice_text).text
        assert assert_politice_text == assert_politice, 'Текст из <Политика персональных данных> не соответствует'
        button_close = self.find(el_doc.button_close)
        button_close.click()
        self.wait(el_auth.outside_map)
        map = self.find(el_auth.outside_map)
        map.click()
        self.wait(el_auth.main_menu)
        menu = self.find(el_auth.main_menu)
        menu.click()
        self.wait(el_doc.documents)
        documents = self.find(el_doc.documents)
        documents.click()
        self.wait(requisites)
        consent = self.find(requisites)
        consent.click()
        self.wait(requisites_text)
        assert_requisites_text = self.find(requisites_text).text
        assert assert_requisites_text == assert_requisites, 'Текст из <Реквизиты> не соответствует'
        button_close = self.find(el_doc.button_close)
        button_close.click()
        self.wait(el_auth.outside_map)

    def tarif(self, tariff_country, assert_text):
        '''Проверка тарифа для страны'''
        self.wait(el_auth.main_menu)
        menu = self.find(el_auth.main_menu)
        menu.click()
        self.wait(el_tariff.tariff_menu)
        tariff = self.find(el_tariff.tariff_menu)
        tariff.click()
        self.wait(tariff_country)
        text_tariff = self.find(tariff_country).text
        assert assert_text == text_tariff, 'Название тарифа не соответствует'
        self.wait(el_tariff.tariff_close)
        close = self.find(el_tariff.tariff_close)
        close.click()

    def add_card_main_button(self, form_number_card, number, form_year_card, year, form_cvc, cvc):
        '''Добавление карты с главной страницы'''
        self.wait(main_button_card)
        button_card = self.find(main_button_card)
        button_card.click()
        self.wait(form_number_card)
        number_card = self.find(form_number_card)
        number_card.send_keys(number)
        year_card = self.find(form_year_card)
        year_card.send_keys(year)
        cvc_card = self.find(form_cvc)
        cvc_card.send_keys(cvc)
        button_send_date_card = self.find(button_pay)
        self.wait(operation_button_ok)
        button_ok = self.find(operation_button_ok)
        button_ok.click()
        self.wait(banner_off)
        banner_close = self.find(banner_off)
        banner_close.click()

    def find_card(self):
        '''Проверка добавленной карты в меню'''
        self.wait(el_auth.main_menu)
        menu = self.find(el_auth.main_menu)
        menu.click()
        self.wait(user_cards)
        cards = self.find(user_cards)
        cards.click()
        self.wait(bin_card)
        self.find(bin_card)
        back = self.find(back_to_map)
        back.click()

    def add_card_menu(self):
        '''Добавление карты через меню'''

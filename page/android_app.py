import time

from selenium.common import TimeoutException

from element_locators import auth_elements as el_auth, doc_elements as el_doc, tariff_elements as el_tariff, card_elements as el_card
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


    def documents_in_russia(self):
        '''Проверка документов у России'''
        self.documents_in_country(
            user_consent=el_doc.russian_consent,
            consent_text=el_doc.russian_consent_text,
            assert_consent=el_doc.assert_russian_consent_text,
            politice_date=el_doc.russian_politice,
            politice_text=el_doc.russian_politice_text,
            assert_politice=el_doc.assert_russian_politice_text,
            requisites=el_doc.russian_requisites,
            requisites_text=el_doc.russian_requisites_text,
            assert_requisites=el_doc.assert_russian_requisites_text
        )

    def documents_in_kazahstan(self):
        '''Проверка документов у Казахстана'''
        self.documents_in_country(
            user_consent=el_doc.kazahstan_consent,
            consent_text=el_doc.kazahstan_consent_text,
            assert_consent=el_doc.assert_kazahstan_consent_text,
            politice_date=el_doc.kazahstan_politice,
            politice_text=el_doc.kazahstan_politice_text,
            assert_politice=el_doc.assert_kazahstan_politice_text,
            requisites=el_doc.kazahstan_requisites,
            requisites_text=el_doc.kazahstan_requisites_text,
            assert_requisites=el_doc.assert_kazahstan_requisites_text
        )

    def documents_in_kirgistan(self):
        '''Проверка документов у Киргизтана'''
        self.documents_in_country(
            user_consent=el_doc.kirgistan_consent,
            consent_text=el_doc.kirgistan_consent_text,
            assert_consent=el_doc.assert_kirgistan_consent_text,
            politice_date=el_doc.kirgistan_politice,
            politice_text=el_doc.kirgistan_politice_text,
            assert_politice=el_doc.assert_kirgiztan_politice_text,
            requisites=el_doc.kirgistan_requisites,
            requisites_text=el_doc.kirgistan_requisites_text,
            assert_requisites=el_doc.assert_kirgistan_requisites_text
        )

    def documents_in_belarussia(self):
        '''Проверка документов у Беларуси'''
        self.documents_in_country(
            user_consent=el_doc.belarussia_consent,
            consent_text=el_doc.belarussia_consent_text,
            assert_consent=el_doc.assert_belarussia_consent_text,
            politice_date=el_doc.belarussia_politice,
            politice_text=el_doc.belarussia_politice_text,
            assert_politice=el_doc.assert_belarussia_politice_text,
            requisites=el_doc.belarussia_requisites,
            requisites_text=el_doc.belarussia_requisites_text,
            assert_requisites=el_doc.assert_belarussia_requisites_text
        )

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

    def add_card_in_russia(self):
        '''Добавление карты для России с главной страницы'''
        self.add_card_main_button(
            form_number_card=el_card.form_number_card_in_russia,
            number=el_card.number_russia,
            form_year_card=el_card.form_year_card_in_russia,
            year=el_card.year_russia,
            form_cvc=el_card.form_cvc_in_russia,
            cvc=el_card.cvc_russia,
            button_pay=el_card.button_pay_in_russia,
            operation_button_ok=el_card.operation_button_ok_in_russia
        )

    def add_card_in_russia_menu(self):
        '''Добавление карты для России из меню'''
        self.add_card_menu(
            form_number_card=el_card.form_number_card_in_russia,
            number=el_card.number_russia,
            form_year_card=el_card.form_year_card_in_russia,
            year=el_card.year_russia,
            form_cvc=el_card.form_cvc_in_russia,
            cvc=el_card.cvc_russia,
            button_pay=el_card.button_pay_in_russia,
            operation_button_ok=el_card.operation_button_ok_in_russia,
            bin_country=el_card.bin_russia
        )

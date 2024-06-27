import time

from selenium.common import TimeoutException

from element_locators import auth_elements as el_auth
from element_locators import card_elements as el_card
from element_locators import doc_elements as el_doc
from element_locators import sub_elements as el_sub
from element_locators import tariff_elements as el_tariff
from fixtures.db_settings import DbConnect
from page.base_app import BaseApp


class AndroidApp(BaseApp):
    '''Класс Андроид устройства'''

    def auth(self, code_phone, phone):
        '''Авторизация пользователя через телефон'''
        self.wait_click(el_auth.login_in_phone)
        self.click_element(el_auth.login_in_phone)
        self.wait_click(el_auth.code_country)
        self.click_element(el_auth.code_country)
        if code_phone == el_auth.kirgistan_code:
            self.wait(el_auth.search_country)
            self.send_keys_element(el_auth.search_country, 'Киргизия')
        self.wait_click(code_phone)
        self.click_element(code_phone)
        self.wait(el_auth.form_phone)
        self.send_keys_element(el_auth.form_phone, phone)
        self.click_element(el_auth.button_send_phone)
        self.wait_click(el_auth.code_input)
        self.click_element(el_auth.code_input)
        self.sms()

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
        time.sleep(2)
        # db_connect = DbConnect()
        # zone_search = db_connect.search_zone(phone=phone)
        # assert zone_search == zone, 'Пользователь создался с другой зоной или при создание зона не добавилась в базу'

    def delete_user(self):
        '''Удаление активного пользователя'''
        self.wait_click(el_auth.main_menu)
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
        self.wait(el_auth.complete_delete_button)
        complete_delete = self.find(el_auth.complete_delete_button)
        complete_delete.click()


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
        self.wait_click(el_auth.main_menu)
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
        )
        self.wait(el_card.operation_button_ok_in_russia)
        button_ok = self.find(el_card.operation_button_ok_in_russia)
        button_ok.click()
        self.wait(el_card.banner_card_ok)
        self.wait(el_card.banner_off)
        banner_close = self.find(el_card.banner_off)
        banner_close.click()

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

    def replace_card_in_russia(self):
        '''Замена карты для России'''
        self.card_replace(
            bin_country=el_card.bin_russia,
            form_number_card=el_card.new_form_number_card_in_russia,
            new_number=el_card.new_number_russia,
            form_year_card=el_card.new_form_year_card_in_russia,
            new_year=el_card.year_russia,
            form_cvc=el_card.new_form_cvc_in_russia,
            new_cvc=el_card.cvc_russia,
            button_pay=el_card.button_pay_in_russia,
            operation_button_ok=el_card.operation_button_ok_in_russia,
            new_bin_country=el_card.new_bin_russia
        )

    def add_card_in_russia_subscription(self):
        '''Добавление карты для России с помощью покупки подписки'''
        self.add_card_in_subscription(
            form_number_card=el_card.form_number_card_in_russia,
            number=el_card.number_russia,
            form_year_card=el_card.form_year_card_in_russia,
            year=el_card.year_russia,
            form_cvc=el_card.form_cvc_in_russia,
            cvc=el_card.cvc_russia,
            button_pay=el_card.button_pay_in_russia,
        )
        self.wait(el_card.operation_button_ok_in_russia)
        button_ok = self.find(el_card.operation_button_ok_in_russia)
        button_ok.click()
        self.wait(el_card.subscription_ok)

    def add_card_in_belarussia(self):
        '''Добавление карты для Беларуси с главной страницы'''
        self.add_card_main_button(
            form_number_card=el_card.form_number_card_in_belarussia,
            number=el_card.number_belarussia,
            form_year_card=el_card.form_year_card_in_belarussia,
            year=el_card.year_belarussia,
            form_cvc=el_card.form_cvc_in_belarussia,
            cvc=el_card.cvc_belarussia,
            button_pay=el_card.button_pay_in_belarussia,
        )
        self.wait(el_card.banner_card_ok)
        time.sleep(2)

    def add_card_in_belarussia_menu(self):
        '''Добавление карты для Беларуси из меню'''
        self.add_card_menu(
            form_number_card=el_card.form_number_card_in_belarussia,
            number=el_card.number_belarussia,
            form_year_card=el_card.form_year_card_in_belarussia,
            year=el_card.year_belarussia,
            form_cvc=el_card.form_cvc_in_belarussia,
            cvc=el_card.cvc_belarussia,
            button_pay=el_card.button_pay_in_belarussia,
            operation_button_ok=el_card.operation_button_ok_in_belarussia,
            bin_country=el_card.bin_belarussia
        )

    def replace_card_in_belarussia(self):
        '''Замена карты для Беларуси'''
        self.card_replace(
            bin_country=el_card.bin_belarussia,
            form_number_card=el_card.form_number_card_in_belarussia,
            new_number=el_card.new_number_belarussia,
            form_year_card=el_card.form_year_card_in_belarussia,
            new_year=el_card.year_belarussia,
            form_cvc=el_card.form_cvc_in_belarussia,
            new_cvc=el_card.cvc_belarussia,
            button_pay=el_card.button_pay_in_belarussia,
            operation_button_ok=el_card.operation_button_ok_in_belarussia,
            new_bin_country=el_card.new_bin_belarussia
        )

    def add_card_in_kazahstan(self):
        '''Добавление карты для Казахстан с главной страницы'''
        self.add_card_main_button(
            form_number_card=el_card.form_number_card_in_kazahstan,
            number=el_card.number_kazahstan,
            form_year_card=el_card.form_year_card_in_kazahstan,
            year=el_card.year_kazahstan,
            form_cvc=el_card.form_cvc_in_kazahstan,
            cvc=el_card.cvc_kazahstan,
            button_pay=el_card.button_pay_in_kazahstan,
        )
        self.wait(el_card.operation_button_ok_in_kazahstan)
        button_ok = self.find(el_card.operation_button_ok_in_kazahstan)
        button_ok.click()
        self.wait(el_card.banner_card_ok)
        time.sleep(2)

    def add_card_in_kazahstan_menu(self):
        '''Добавление карты для Казахстана из меню'''
        self.add_card_menu(
            form_number_card=el_card.form_number_card_in_kazahstan,
            number=el_card.number_kazahstan,
            form_year_card=el_card.form_year_card_in_kazahstan,
            year=el_card.year_kazahstan,
            form_cvc=el_card.form_cvc_in_kazahstan,
            cvc=el_card.cvc_kazahstan,
            button_pay=el_card.button_pay_in_kazahstan,
            operation_button_ok=el_card.operation_button_ok_in_kazahstan,
            bin_country=el_card.bin_kazahstan
        )

    def replace_card_in_kazahstan(self):
        '''Замена карты для Казахстана'''
        self.card_replace(
            bin_country=el_card.bin_kazahstan,
            form_number_card=el_card.form_number_card_in_kazahstan,
            new_number=el_card.new_number_kazahstan,
            form_year_card=el_card.form_year_card_in_kazahstan,
            new_year=el_card.year_kazahstan,
            form_cvc=el_card.form_cvc_in_kazahstan,
            new_cvc=el_card.cvc_kazahstan,
            button_pay=el_card.button_pay_in_kazahstan,
            operation_button_ok=el_card.operation_button_ok_in_kazahstan,
            new_bin_country=el_card.new_bin_kazahstan
        )

    def add_card_in_kirgistan(self):
        '''Добавление карты для Киргизии с главной страницы'''
        self.add_card_main_button(
            form_number_card=el_card.form_number_card_in_kirgistan,
            number=el_card.number_kirgistan,
            form_year_card_month=el_card.form_year_card_in_kirgistan_month,
            year_month=el_card.year_kirgistan_month,
            form_year_card=el_card.form_year_card_in_kirgistan_year,
            year=el_card.year_kirgistan_year,
            form_cvc=el_card.form_cvc_in_kirgistan,
            cvc=el_card.cvc_kirgistan,
            button_pay=el_card.button_pay_in_kirgistan,
        )
        self.wait(el_card.banner_card_ok)
        time.sleep(2)

    def add_card_in_kirgistan_menu(self):
        '''Добавление карты для Киргизиииз меню'''
        self.add_card_menu(
            bin_country=el_card.bin_kirgistan,
            form_number_card=el_card.form_number_card_in_kirgistan,
            number=el_card.number_kirgistan,
            form_year_card_month=el_card.form_year_card_in_kirgistan_month,
            year_month=el_card.year_kirgistan_month,
            form_year_card=el_card.form_year_card_in_kirgistan_year,
            year=el_card.year_kirgistan_year,
            form_cvc=el_card.form_cvc_in_kirgistan,
            cvc=el_card.cvc_kirgistan,
            button_pay=el_card.button_pay_in_kirgistan,
        )

    def replace_card_in_kirgistan(self):
        '''Замена карты для Киргизии'''
        self.card_replace(
            bin_country=el_card.bin_kirgistan,
            form_number_card=el_card.form_number_card_in_kirgistan,
            new_number=el_card.new_number_kirgistan,
            form_year_card_month=el_card.form_year_card_in_kirgistan_month,
            year_month=el_card.new_year_kirgistan_month,
            form_year_card=el_card.form_year_card_in_kirgistan_year,
            new_year=el_card.new_year_kirgistan_year,
            form_cvc=el_card.form_cvc_in_kirgistan,
            new_cvc=el_card.new_cvc_kirgistan,
            button_pay=el_card.button_pay_in_kirgistan,
            new_bin_country=el_card.new_bin_kirgistan
        )

    def pay_subscription_on_map(self):
        '''Покупка подписки с главного экрана, проверка счетчика на главном экране,в разделе подписки, в меню'''
        self.wait(el_auth.subscription)
        sub_button = self.find(el_auth.subscription)
        sub_button.click()
        self.wait(el_card.subscription_add)
        add_sub_button = self.find(el_card.subscription_add)
        add_sub_button.click()
        self.wait(el_card.subscription_ok)
        self.wait(el_sub.button_subscription)
        count_button = self.find(el_sub.button_subscription)
        assert count_button.text == el_sub.access_button, 'На кнопке подписки не отображается количество аренд'
        self.wait_click(el_sub.subscriptions)
        button = self.find(el_sub.subscriptions)
        button.click()
        self.wait(el_sub.count_subscription)
        count = self.find(el_sub.count_subscription)
        assert count.text == el_sub.access_count, 'В разделе подписки не соответсвует количество аренд'
        close = self.find(el_sub.off_subscription)
        close.click()
        self.wait(el_auth.main_map)
        self.wait(el_auth.main_menu)
        menu = self.find(el_auth.main_menu)
        menu.click()
        self.wait(el_sub.count_subscription_button)
        sub_button_menu = self.find(el_sub.count_subscription_button)
        assert sub_button_menu.text == el_sub.access_count, 'В главном меню не отображается количество аренд по подписке'
        back = self.find(el_sub.back_map)
        back.click()
        self.wait(el_auth.main_map)

    def pay_subscription_on_and_off(self):
        '''Покупка подписки на главном экране, отказ от автопродление, автопродление'''
        self.wait(el_auth.subscription)
        sub_button = self.find(el_auth.subscription)
        sub_button.click()
        self.wait(el_card.subscription_add)
        add_sub_button = self.find(el_card.subscription_add)
        add_sub_button.click()
        self.wait(el_card.subscription_ok)
        self.wait_click(el_sub.subscriptions)
        button = self.find(el_sub.subscriptions)
        button.click()
        self.wait(el_sub.off_subscription)
        off_subscription = self.find(el_sub.button_off_subscription)
        off_subscription.click()
        self.wait(el_sub.on_delete)
        delete_sub = self.find(el_sub.on_delete)
        delete_sub.click()
        self.wait(el_sub.subscription_off_text)
        text_off_subscription = self.find(el_sub.subscription_off_text).text
        assert text_off_subscription == el_sub.access_text, 'Нет уведомление об отключение автопродления'
        back_sub = self.find(el_sub.button_return_subscription)
        back_sub.click()
        self.wait(el_card.subscription_add)
        add_sub_button = self.find(el_card.subscription_add)
        add_sub_button.click()
        self.wait(el_card.subscription_ok)

    def pay_subscription_on_banner(self):
        '''Покупка подписки с через баннер после привязки карты, проверка счетчика на главном экране,в разделе подписки, в меню'''
        self.add_card_main_button(
            form_number_card=el_card.form_number_card_in_russia,
            number=el_card.number_russia,
            form_year_card=el_card.form_year_card_in_russia,
            year=el_card.year_russia,
            form_cvc=el_card.form_cvc_in_russia,
            cvc=el_card.cvc_russia,
            button_pay=el_card.button_pay_in_russia,
        )
        self.wait(el_card.operation_button_ok_in_russia)
        button_ok = self.find(el_card.operation_button_ok_in_russia)
        button_ok.click()
        self.wait(el_sub.banner_subscription_pay)
        banner_pay = self.find(el_sub.banner_subscription_pay)
        banner_pay.click()
        self.wait(el_card.subscription_add)
        add_sub_button = self.find(el_card.subscription_add)
        add_sub_button.click()
        self.wait(el_card.subscription_ok)
        self.wait(el_sub.button_subscription)
        count_button = self.find(el_sub.button_subscription)
        assert count_button.text == el_sub.access_button, 'На кнопке подписки не отображается количество аренд'
        self.wait_click(el_sub.subscriptions)
        button = self.find(el_sub.subscriptions)
        button.click()
        self.wait(el_sub.count_subscription)
        count = self.find(el_sub.count_subscription)
        assert count.text == el_sub.access_count, 'В разделе подписки не соответсвует количество аренд'
        close = self.find(el_sub.off_subscription)
        close.click()
        self.wait(el_auth.main_map)
        self.wait(el_auth.main_menu)
        menu = self.find(el_auth.main_menu)
        menu.click()
        self.wait(el_sub.count_subscription_button)
        sub_button_menu = self.find(el_sub.count_subscription_button)
        assert sub_button_menu.text == el_sub.access_count, 'В главном меню не отображается количество аренд по подписке'
        back = self.find(el_sub.back_map)
        back.click()
        self.wait(el_auth.main_map)

    def pay_subscription_on_menu(self):
        '''Покупка подписки в меню, проверка счетчика на главном экране,в разделе подписки, в меню'''
        self.wait(el_auth.main_menu)
        menu = self.find(el_auth.main_menu)
        menu.click()
        self.wait(el_sub.subscriptions_menu)
        sub_menu = self.find(el_sub.subscriptions_menu)
        sub_menu.click()
        self.wait(el_card.subscription_add)
        add_sub_button = self.find(el_card.subscription_add)
        add_sub_button.click()
        self.wait(el_card.subscription_ok)
        self.wait(el_sub.button_subscription)
        count_button = self.find(el_sub.button_subscription)
        assert count_button.text == el_sub.access_button, 'На кнопке подписки не отображается количество аренд'
        self.wait_click(el_sub.subscriptions)
        button = self.find(el_sub.subscriptions)
        button.click()
        self.wait(el_sub.count_subscription)
        count = self.find(el_sub.count_subscription)
        assert count.text == el_sub.access_count, 'В разделе подписки не соответсвует количество аренд'
        close = self.find(el_sub.off_subscription)
        close.click()
        self.wait(el_auth.main_map)
        self.wait(el_auth.main_menu)
        menu = self.find(el_auth.main_menu)
        menu.click()
        self.wait(el_sub.count_subscription_button)
        sub_button_menu = self.find(el_sub.count_subscription_button)
        assert sub_button_menu.text == el_sub.access_count, 'В главном меню не отображается количество аренд по подписке'
        back = self.find(el_sub.back_map)
        back.click()
        self.wait(el_auth.main_map)
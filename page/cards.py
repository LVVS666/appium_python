from element_locators import card_elements as el_card
from element_locators import auth_elements as el_auth
from page.auth import Auth
from page.base_app import BaseApp


class Cards(BaseApp, Auth):
    '''Класс банковских карт'''
    def add_card_main_button(self,
                             form_number_card,
                             number,
                             form_year_card=None,
                             year=None,
                             form_year_card_month = None,
                             year_month = None,
                             form_cvc=None,
                             cvc=None,
                             button_pay=None):
        '''Добавление карты с главной страницы'''
        self.click_element(el_card.main_button_card)
        if number == el_card.number_kirgistan:
            self.send_keys_element(form_number_card, number)
            self.app.press_keycode(66)
            self.send_keys_element_click(form_year_card_month, year_month)
            self.click_element(el_card.accec_09)
            self.send_keys_element_click(form_year_card, year)
            self.click_element(el_card.accec_2026)
            self.send_keys_element(form_cvc, cvc)
            self.click_element(button_pay)
        else:
            self.send_keys_element(form_number_card, number)
            self.send_keys_element(form_year_card, year)
            self.send_keys_element(form_cvc, cvc)
            self.click_element(button_pay)

    def find_card(self, bin_country):
        '''Проверка добавленной карты в меню'''
        self.click_element(el_auth.main_menu)
        self.click_element(el_card.user_cards)
        self.wait(el_card.bin_card)
        access_bin = self.find(el_card.bin_card).text
        assert access_bin == bin_country, 'Номер добавленной карты не совпадает'
        self.click_element(el_card.back_to_map)

    def add_card_menu(self,
                      form_number_card,
                      number,
                      form_year_card,
                      year,
                      form_cvc,
                      cvc,
                      button_pay,
                      bin_country,
                      operation_button_ok=None,
                      form_year_card_month=None,
                      year_month=None):
        '''Добавление карты через меню'''
        self.click_element(el_auth.main_menu)
        self.click_element(el_card.user_cards)
        self.click_element(el_card.add_card)
        if number == el_card.number_kirgistan:
            self.send_keys_element(form_number_card, number)
            self.app.press_keycode(66)
            self.send_keys_element_click(form_year_card_month, year_month)
            self.click_element(el_card.accec_09)
            self.send_keys_element_click(form_year_card, year)
            self.click_element(el_card.accec_2026)
            self.send_keys_element(form_cvc, cvc)
            self.click_element(button_pay)
        else:
            self.send_keys_element(form_number_card, number)
            self.send_keys_element(form_year_card, year)
            self.send_keys_element(form_cvc, cvc)
            self.click_element(button_pay)
        if number != el_card.number_belarussia and number != el_card.number_kirgistan:
            self.click_element(operation_button_ok)
        self.wait(el_card.banner_card_ok)
        self.wait(el_card.bin_card)
        access_bin = self.find(el_card.bin_card).text
        assert access_bin == bin_country, 'Номер добавленной карты не совпадает'
        self.click_element(el_card.back_to_map)

    def add_card_in_subscription(self,
                                 form_number_card,
                                 number, form_year_card,
                                 year,
                                 form_cvc,
                                 cvc,
                                 button_pay):
        '''Привязка карты через оформление подписки'''
        self.click_element(el_auth.subscription)
        self.click_element(el_card.subscription_add)
        self.send_keys_element(form_number_card, number)
        self.send_keys_element(form_year_card, year)
        self.send_keys_element(form_cvc, cvc)
        self.click_element(button_pay)

    def card_replace(self,
                     bin_country,
                     form_number_card,
                     new_number,
                     form_year_card,
                     new_year,
                     form_cvc,
                     new_cvc,
                     button_pay,
                     new_bin_country,
                     operation_button_ok=None,
                     form_year_card_month=None,
                     year_month=None):
        '''Замена карты'''
        self.click_element(el_auth.main_menu)
        self.click_element(el_card.user_cards)
        self.wait(el_card.bin_card)
        access_bin = self.find(el_card.bin_card).text
        assert access_bin == bin_country, 'Номер добавленной карты не совпадает'
        self.click_element(el_card.add_card)
        if new_number == el_card.new_number_russia:
            self.click_element(el_card.replace_new_card)
        if new_number == el_card.new_number_kirgistan:
            self.send_keys_element(form_number_card, new_number)
            self.app.press_keycode(66)
            self.send_keys_element_click(form_year_card_month, year_month)
            self.click_element(el_card.accec_05)
            self.send_keys_element_click(form_year_card, new_year)
            self.click_element(el_card.accec_2027)
            self.send_keys_element(form_cvc, new_cvc)
            self.click_element(button_pay)
        if new_number != el_card.new_number_kirgistan:
            self.send_keys_element(form_year_card, new_year)
            self.send_keys_element(form_number_card, new_number)
            self.send_keys_element(form_cvc,new_cvc)
            self.click_element(button_pay)
        if new_number != el_card.new_number_belarussia and new_number != el_card.new_number_kirgistan:
            self.click_element(operation_button_ok)
        self.wait(el_card.banner_card_ok)
        self.wait(el_card.bin_card)
        access_new_bin = self.find(el_card.bin_card).text
        assert access_new_bin == new_bin_country, 'Номер добавленной карты не совпадает'
        self.click_element(el_card.back_to_map)

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
        self.click_element(el_card.operation_button_ok_in_russia)
        self.wait(el_card.banner_card_ok)
        self.click_element(el_card.banner_off)

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
        self.click_element(el_card.operation_button_ok_in_russia)
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
        self.click_element(el_card.operation_button_ok_in_kazahstan)
        self.wait(el_card.banner_card_ok)

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

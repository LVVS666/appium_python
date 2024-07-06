from element_locators import card_elements as el_card
from page.auth import Auth
from page.base_app import BaseApp


class Cards(BaseApp, Auth):
    '''Класс банковских карт'''
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

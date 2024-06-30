import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from element_locators import auth_elements as el_auth
from element_locators import card_elements as el_card
from element_locators import doc_elements as el_doc


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
        self.click_element(el_auth.outside_map)
        self.click_element(el_auth.main_menu)
        self.click_element(el_doc.documents)
        self.click_element(user_consent)
        self.wait(consent_text)
        assert_consent_text = self.find(consent_text).text
        assert assert_consent_text == assert_consent, 'Текст из <Пользовательского соглашения> не соответствует'
        self.click_element(el_doc.button_close)
        self.click_element(el_auth.outside_map)
        self.click_element(el_auth.main_menu)
        self.click_element(el_doc.documents)
        self.click_element(politice_date)
        self.wait(politice_text)
        assert_politice_text = self.find(politice_text).text
        assert assert_politice_text == assert_politice, 'Текст из <Политика персональных данных> не соответствует'
        self.click_element(el_doc.button_close)
        self.click_element(el_auth.outside_map)
        self.click_element(el_auth.main_menu)
        self.click_element(el_doc.documents)
        self.click_element(requisites)
        self.wait(requisites_text)
        assert_requisites_text = self.find(requisites_text).text
        assert assert_requisites_text == assert_requisites, 'Текст из <Реквизиты> не соответствует'
        self.click_element(el_doc.button_close)
        self.wait(el_auth.outside_map)

    def sms(self):
        '''Ввод смс подтверждения'''
        self.app.press_keycode(7)
        self.app.press_keycode(7)
        self.app.press_keycode(7)
        self.app.press_keycode(8)

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
        time.sleep(2)
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
        time.sleep(2)
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
        time.sleep(2)
        self.click_element(el_card.back_to_map)

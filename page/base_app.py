from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from element_locators import auth_elements as el_auth, doc_elements as el_doc


class BaseApp:
    '''Базовый класс работы с андроидом'''

    def __init__(self, app):
        self.app = app

    def find(self, args):
        '''Поиск элемента'''
        return self.app.find_element(*args)

    def wait(self, args):
        '''Ожидание видимого элемента'''
        WebDriverWait(self.app, 10).until(EC.presence_of_element_located(args))

    def wait_click(self, args):
        '''Ожидание кликабельного элемента'''
        WebDriverWait(self.app, 10).until(EC.element_to_be_clickable(args))

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

    def sms(self):
        '''Ввод смс подтверждения'''
        self.app.press_keycode(7)
        self.app.press_keycode(7)
        self.app.press_keycode(7)
        self.app.press_keycode(8)

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
        button_send_date_card.click()
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

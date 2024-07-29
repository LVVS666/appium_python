from element_locators import auth_elements as el_auth
from element_locators import sub_elements as el_sub
from element_locators import tariff_elements as el_tariff
from element_locators import menu_elements as el_menu
from page.auth import Auth


class MainMenu(Auth):
    '''Класс Андроид устройства'''
    def tarif(self, tariff_country, assert_text):
        '''Проверка тарифа для страны'''
        self.click_element(el_auth.main_menu)
        self.click_element(el_tariff.tariff_menu)
        self.wait(tariff_country)
        text_tariff = self.find(tariff_country).text
        assert assert_text == text_tariff, 'Название тарифа не соответствует'
        self.click_element(el_tariff.tariff_close)

    def checkout_menu(self, auth=False):
        '''Проверка меню'''
        self.click_element(el_menu.main_menu)
        if auth is False:
            self.click_element(el_menu.out_back_map)
            self.click_element(el_menu.main_menu)
            self.click_element(el_menu.auth)
            self.wait(el_menu.auth_access)
            assert self.find(el_menu.auth_access).text == el_menu.text_auth, 'Кнопка авторизации не сработала'
            self.click_element(el_menu.out_back_map)
        elif auth is True:
            self.click_element(el_menu.profile)
            self.wait(el_menu.profile_content)
            assert self.find(el_menu.profile_content), 'Кнопка профиль не сработала'
            self.click_element(el_menu.back)
            self.click_element(el_menu.main_menu)
            self.click_element(el_menu.pay)
            self.wait(el_menu.pay_content)
            assert self.find(el_menu.pay_content), 'Кнопка способы оплаты не сработала'
            self.click_element(el_menu.main_menu)
            self.click_element(el_menu.main_menu)
            self.click_element(el_menu.subscription)
            self.wait(el_sub.banner_subscription_pay)
            assert self.find(el_sub.banner_subscription_pay), 'Кнопка подписка не сработала'
            self.click_element(el_menu.main_menu)
            self.click_element(el_menu.main_menu)
            self.click_element(el_menu.partners)
            self.wait(el_menu.partners_content)
            assert self.find(el_menu.partners_content), 'Кнопка акции партнеров не сработала'
            self.click_element(el_menu.main_menu)
            self.click_element(el_menu.main_menu)
            self.click_element(el_menu.tariff)
            self.wait(el_menu.tariff_content)
            assert self.find(el_menu.tariff_content), 'Кнопка тарифы не сработала'
            self.click_element(el_menu.main_menu)
            self.click_element(el_menu.main_menu)
            self.click_element(el_menu.bonuses)
            self.wait(el_menu.bonus_access)
            assert self.find(el_menu.bonus_access).text == el_menu.text_bonus, 'Кнопка бонусы не сработала'
            self.click_element(el_menu.main_menu)
        self.click_element(el_menu.main_menu)
        self.click_element(el_menu.support)
        self.wait(el_menu.support_content)
        assert self.find(el_menu.support_content), 'Кнопка поддержки не сработала'
        self.app.tap([(el_menu.x, el_menu.y)])
        self.click_element(el_menu.main_menu)
        self.click_element(el_menu.documents)
        self.wait(el_menu.doc_access)
        assert self.find(el_menu.doc_access).text == el_menu.text_doc, 'Кнопка документов не сработала'
        self.click_element(el_menu.document_back)
        self.click_element(el_menu.out_back_map)
        self.click_element(el_menu.main_menu)
        self.click_element(el_menu.franchizing)
        self.wait(el_menu.main_banner)
        assert self.find(el_menu.main_banner), 'Кнопка франшизы не сработала'
        self.click_element(el_menu.main_menu)
        self.click_element(el_menu.out_back_map)
        self.click_element(el_menu.main_menu)
        self.click_element(el_menu.about)
        self.wait(el_menu.about_content)
        assert self.find(el_menu.about_content), 'Кнопка о приложение не сработала'
        self.click_element(el_menu.back)
        self.click_element(el_menu.out_back_map)

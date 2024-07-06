from element_locators import auth_elements as el_auth
from element_locators import card_elements as el_card
from element_locators import sub_elements as el_sub
from page.auth import Auth
from page.base_app import BaseApp
from page.cards import Cards


class Subscriptions(BaseApp, Auth, Cards):
    '''Класс Подписок'''

    def pay_subscription_on_map(self):
        '''Покупка подписки с главного экрана, проверка счетчика на главном экране,в разделе подписки, в меню'''
        self.click_element(el_auth.subscription)
        self.click_element(el_card.subscription_add)
        self.wait(el_card.subscription_ok)
        self.wait(el_sub.button_subscription)
        count_button = self.find(el_sub.button_subscription)
        assert count_button.text == el_sub.access_button, 'На кнопке подписки не отображается количество аренд'
        self.click_element(el_sub.subscriptions)
        self.wait(el_sub.count_subscription)
        count = self.find(el_sub.count_subscription)
        assert count.text == el_sub.access_count, 'В разделе подписки не соответсвует количество аренд'
        self.click_element(el_sub.off_subscription)
        self.wait(el_auth.main_map)
        self.click_element(el_auth.main_menu)
        self.wait(el_sub.count_subscription_button)
        sub_button_menu = self.find(el_sub.count_subscription_button)
        assert sub_button_menu.text == el_sub.access_count, 'В главном меню не отображается количество аренд по подписке'
        self.click_element(el_sub.back_map)
        self.wait(el_auth.main_map)

    def pay_subscription_on_and_off(self):
        '''Покупка подписки на главном экране, отказ от автопродление, автопродление'''
        self.click_element(el_auth.subscription)
        self.click_element(el_card.subscription_add)
        self.wait(el_card.subscription_ok)
        self.click_element(el_sub.subscriptions)
        self.click_element(el_sub.off_subscription)
        self.click_element(el_sub.on_delete)
        self.wait(el_sub.subscription_off_text)
        text_off_subscription = self.find(el_sub.subscription_off_text).text
        assert text_off_subscription == el_sub.access_text, 'Нет уведомление об отключение автопродления'
        self.click_element(el_sub.button_return_subscription)
        self.click_element(el_card.subscription_add)
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
        self.click_element(el_card.operation_button_ok_in_russia)
        self.click_element(el_sub.banner_subscription_pay)
        self.click_element(el_card.subscription_add)
        self.wait(el_card.subscription_ok)
        self.wait(el_sub.button_subscription)
        count_button = self.find(el_sub.button_subscription)
        assert count_button.text == el_sub.access_button, 'На кнопке подписки не отображается количество аренд'
        self.click_element(el_sub.subscriptions)
        self.wait(el_sub.count_subscription)
        count = self.find(el_sub.count_subscription)
        assert count.text == el_sub.access_count, 'В разделе подписки не соответсвует количество аренд'
        self.click_element(el_sub.off_subscription)
        self.wait(el_auth.main_map)
        self.click_element(el_auth.main_menu)
        self.wait(el_sub.count_subscription_button)
        sub_button_menu = self.find(el_sub.count_subscription_button)
        assert sub_button_menu.text == el_sub.access_count, 'В главном меню не отображается количество аренд по подписке'
        self.click_element(el_sub.back_map)
        self.wait(el_auth.main_map)

    def pay_subscription_on_menu(self):
        '''Покупка подписки в меню, проверка счетчика на главном экране,в разделе подписки, в меню'''
        self.click_element(el_auth.main_menu)
        self.click_element(el_sub.subscriptions_menu)
        self.click_element(el_card.subscription_add)
        self.wait(el_card.subscription_ok)
        self.wait(el_sub.button_subscription)
        count_button = self.find(el_sub.button_subscription)
        assert count_button.text == el_sub.access_button, 'На кнопке подписки не отображается количество аренд'
        self.click_element(el_sub.subscriptions)
        self.wait(el_sub.count_subscription)
        count = self.find(el_sub.count_subscription)
        assert count.text == el_sub.access_count, 'В разделе подписки не соответсвует количество аренд'
        self.click_element(el_sub.off_subscription)
        self.wait(el_auth.main_map)
        self.click_element(el_auth.main_menu)
        self.wait(el_sub.count_subscription_button)
        sub_button_menu = self.find(el_sub.count_subscription_button)
        assert sub_button_menu.text == el_sub.access_count, 'В главном меню не отображается количество аренд по подписке'
        self.click_element(el_sub.back_map)
        self.wait(el_auth.main_map)

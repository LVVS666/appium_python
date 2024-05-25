from page.android_app import AndroidApp
from element_locators import auth_elements as el_auth, card_elements as el_card


def test_add_card_in_russia_main(driver_android):
    '''Добавление карты, для России, через кнопку на главном экране'''
    app_login = AndroidApp(driver_android)
    app_login.registration(code_phone=el_auth.russian_code, country=el_auth.russia, phone=el_auth.rus_kz_phone)
    app_login.add_card_in_russia()
    app_login.find_card(bin_country=el_card.bin_russia)
    app_login.delete_user()


def test_add_card_in_russia_menu(driver_android):
    '''Добавление карты, для России, через меню'''
    app_login = AndroidApp(driver_android)
    app_login.registration(code_phone=el_auth.russian_code, country=el_auth.russia, phone=el_auth.rus_kz_phone)
    app_login.add_card_in_russia_menu()
    app_login.delete_user()
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


def test_add_card_in_russia_subscription(driver_android):
    '''Добавление карты, для России, через покупку подписки'''
    app_login = AndroidApp(driver_android)
    app_login.registration(code_phone=el_auth.russian_code, country=el_auth.russia, phone=el_auth.rus_kz_phone)
    app_login.add_card_in_russia_subscription()
    app_login.find_card(bin_country=el_card.bin_russia)
    app_login.delete_user()


def test_add_card_in_kazahstan_main(driver_android):
    '''Добавление карты, для Казахстана, через кнопку на главном экране'''
    app_login = AndroidApp(driver_android)
    app_login.registration(code_phone=el_auth.kazahstan_code, country=el_auth.kazahstan, phone=el_auth.rus_kz_phone)
    app_login.add_card_in_kazahstan()
    app_login.find_card(bin_country=el_card.bin_kazahstan)
    app_login.delete_user()


def test_add_card_in_kazahstan_menu(driver_android):
    '''Добавление карты, для Казахстана, через меню'''
    app_login = AndroidApp(driver_android)
    app_login.registration(code_phone=el_auth.kazahstan_code, country=el_auth.kazahstan, phone=el_auth.rus_kz_phone)
    app_login.add_card_in_kazahstan_menu()
    app_login.delete_user()


def test_add_card_in_belarussia_main(driver_android):
    '''Добавление карты, для Беларуси, через кнопку на главном экране'''
    app_login = AndroidApp(driver_android)
    app_login.registration(code_phone=el_auth.belarussia_code, country=el_auth.belarussia, phone=el_auth.bld_kgz_phone)
    app_login.add_card_in_belarussia()
    app_login.find_card(bin_country=el_card.bin_belarussia)
    app_login.delete_user()


def test_add_card_in_belarussia_menu(driver_android):
    '''Добавление карты, для Беларуси, через меню'''
    app_login = AndroidApp(driver_android)
    app_login.registration(code_phone=el_auth.belarussia_code, country=el_auth.belarussia, phone=el_auth.bld_kgz_phone)
    app_login.add_card_in_belarussia_menu()
    app_login.delete_user()

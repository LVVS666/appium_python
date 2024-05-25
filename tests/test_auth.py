from element_locators import auth_elements as el_auth
from page.android_app import AndroidApp


def test_registration_in_phone_to_russian_on_logout(driver_android):
    '''Регистрация через телефон для России, после Логаут'''
    app_login = AndroidApp(driver_android)
    app_login.registration(code_phone=el_auth.russian_code, country=el_auth.russia, phone=el_auth.rus_kz_phone)
    app_login.exit()


def test_auth_in_phone_to_russian_on_delete(driver_android):
    '''Авторизация через телефон для России, после удаление аккаунта'''
    app_login = AndroidApp(driver_android)
    app_login.auth(code_phone=el_auth.russian_code, phone=el_auth.rus_kz_phone)
    app_login.button_sub()
    app_login.button_bon()
    app_login.delete_user()


def test_registration_in_phone_to_belarussia_on_delete(driver_android):
    '''Регистрация через телефон для Беларуссии, после удаление аккаунта'''
    app_login = AndroidApp(driver_android)
    app_login.registration(code_phone=el_auth.belarussia_code, country=el_auth.belarussia, phone=el_auth.bld_kgz_phone)
    app_login.not_button_sub()
    app_login.not_button_bon()
    app_login.delete_user()


def test_registration_in_phone_to_kazahstan_on_delete(driver_android):
    '''Регистрация через телефон для Казахстана, после удаление аккаунта'''
    app_login = AndroidApp(driver_android)
    app_login.registration(code_phone=el_auth.kazahstan_code, country=el_auth.kazahstan, phone=el_auth.rus_kz_phone)
    app_login.not_button_sub()
    app_login.not_button_bon()
    app_login.delete_user()


def test_registration_in_phone_to_kirgistan_on_delete(driver_android):
    '''Регистрация через телефон для Киргизии, после удаление аккаунта'''
    app_login = AndroidApp(driver_android)
    app_login.registration(code_phone=el_auth.kirgistan_code, country=el_auth.kirgistan, phone=el_auth.bld_kgz_phone)
    app_login.not_button_sub()
    app_login.button_bon()
    app_login.delete_user()


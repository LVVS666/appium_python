from element_locators import auth_elements as el
from page.login_app import LoginApp


def test_registration_in_phone_to_russian_on_logout(driver_android):
    '''Регистрация через телефон для России, после Логаут'''
    app_login = LoginApp(driver_android)
    app_login.registration(code_phone=el.russian_code, country=el.russia, phone=el.rus_kz_phone)
    app_login.exit()


def test_auth_in_phone_to_russian_on_delete(driver_android):
    '''Авторизация через телефон для России, после удаление аккаунта'''
    app_login = LoginApp(driver_android)
    app_login.auth(code_phone=el.russian_code, country=el.russia, phone=el.rus_kz_phone)
    app_login.button_sub()
    app_login.button_bon()
    app_login.delete_user()


def test_registration_in_phone_to_belarussia_on_delete(driver_android):
    '''Регистрация через телефон для Беларуссии, после удаление аккаунта'''
    app_login = LoginApp(driver_android)
    app_login.registration(code_phone=el.belarussia_code, country=el.belarussia, phone=el.bld_kgz_phone)
    app_login.delete_user()


def test_registration_in_phone_to_kazahstan_on_delete(driver_android):
    '''Регистрация через телефон для Казахстана, после удаление аккаунта'''
    app_login = LoginApp(driver_android)
    app_login.registration(code_phone=el.kazahstan_code, country=el.kazahstan, phone=el.rus_kz_phone)
    app_login.delete_user()


def test_registration_in_phone_to_kirgistan_on_delete(driver_android):
    '''Регистрация через телефон для Киргизии, после удаление аккаунта'''
    app_login = LoginApp(driver_android)
    app_login.registration(code_phone=el.kirgistan_code, country=el.kirgistan, phone=el.bld_kgz_phone)
    app_login.button_bon()
    app_login.delete_user()


def test_list_country_in_doc(driver_android):
    '''Проверка отображения содержимого раздела документов'''
    app_login = LoginApp(driver_android)
    app_login.registration(code_phone=el.russian_code, country=el.russia, phone=el.rus_kz_phone)
    app_login.documents()
    app_login.delete_user()

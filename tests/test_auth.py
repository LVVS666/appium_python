from element_locators import auth_elements as el
from page.login_app import LoginApp


def test_auth_in_phone_to_russian(driver_android):
    app_login = LoginApp(driver_android)
    app_login.auth(code_phone=el.russian_code, country=el.russia, phone='9232769943')
    app_login.delete_user()


def test_auth_in_phone_to_belarussia(driver_android):
    app_login = LoginApp(driver_android)
    app_login.auth(code_phone=el.belarussia_code, country=el.belarussia, phone='255108000')
    app_login.delete_user()


def test_auth_in_phone_to_kazahstan(driver_android):
    app_login = LoginApp(driver_android)
    app_login.auth(code_phone=el.kazahstan_code, country=el.kazahstan, phone='9232769944')
    app_login.delete_user()

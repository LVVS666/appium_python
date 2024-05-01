from page.login_app import LoginApp
from element_locators import auth_elements as el


def test_auth_in_phone_to_russian(driver_android):
    app_login = LoginApp(driver_android)
    app_login.auth(el.russian_code, phone='9232769943')


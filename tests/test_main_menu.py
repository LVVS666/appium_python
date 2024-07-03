from element_locators import auth_elements as el_auth
from page.android_app import AndroidApp


def test_not_auth_menu(driver_android):
    '''Проверка разделов бокового меню у неавторизованного пользователя'''
    app_login = AndroidApp(driver_android)
    app_login.checkout_menu()


def test_auth_menu(driver_android):
    '''Проверка разделов бокового меню у авторизованного пользователя'''
    app_login = AndroidApp(driver_android)
    app_login.registration(code_phone=el_auth.russian_code, phone=el_auth.rus_kz_phone, country=el_auth.russia)
    app_login.checkout_menu(auth=True)
    app_login.delete_user()

import pytest
from element_locators import auth_elements as el_auth
from page.android_app import AndroidApp
from appium import webdriver
from appium.options.android import UiAutomator2Options

# Настройки для двух устройств
capabilities_android_1 = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    "appPackage": "ru.berizaryad.android.staging",
    "appActivity": "ru.berizaryad.android.presentation.main.DrawerMainActivity",
    'udid': 'RZ8MB1Z8PHX',
    'language': 'ru',
    'noReset': False,
    'locale': 'RU',
    'autoGrantPermissions': True
}
capabilities_android_2 = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    "appPackage": "ru.berizaryad.android.staging",
    "appActivity": "ru.berizaryad.android.presentation.main.DrawerMainActivity",
    'language': 'ru',
    'udid': 'e1e86273',
    'noReset': False,
    'locale': 'RU',
    'autoGrantPermissions': True
}
appium_server_url_1 = 'http://localhost:4723'
appium_server_url_2 = 'http://localhost:4725'


@pytest.fixture()
def driver_android_1():
    app_driver = webdriver.Remote(
        appium_server_url_1,
        options=UiAutomator2Options().load_capabilities(capabilities_android_1)
    )
    yield app_driver
    if app_driver.session_id:
        app_driver.quit()


@pytest.fixture()
def driver_android_2():
    app_driver = webdriver.Remote(
        appium_server_url_2,
        options=UiAutomator2Options().load_capabilities(capabilities_android_2)
    )
    yield app_driver
    if app_driver.session_id:
        app_driver.quit()


# Тесты
def test_registration_in_phone_to_belarussia_on_delete(driver_android_1):
    '''Регистрация через телефон для Беларуссии, после удаление аккаунта'''
    app_login = AndroidApp(driver_android_1)
    app_login.registration(
        code_phone=el_auth.belarussia_code,
        country=el_auth.belarussia,
        phone=el_auth.bld_kgz_phone,
    )
    app_login.not_button_sub()
    app_login.not_button_bon()
    app_login.delete_user()


def test_registration_in_phone_to_kazahstan_on_delete(driver_android_2):
    '''Регистрация через телефон для Казахстана, после удаление аккаунта'''
    app_login = AndroidApp(driver_android_2)
    app_login.registration(
        code_phone=el_auth.kazahstan_code,
        country=el_auth.kazahstan,
        phone=el_auth.rus_kz_phone,
    )
    app_login.not_button_sub()
    app_login.not_button_bon()
    app_login.delete_user()

# также нужно прокинуть по аппиум серверу на порт appium http://localhost:4725 и appium http://localhost:4723
# pytest -n 2 tests/test_async_android.py - команда для запуска
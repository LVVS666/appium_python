import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

capabilities_ios = {
    'platformName': 'iOS',
    'automationName': 'XCUITest',
    'deviceName': 'iPhone 8',
    'udid': 'a89659cb25d7f0151803302b0bfa8a66909115f4',
    'platformVersion': '16.7',
    'app': 'com.berizaryad.dev2',
    'language': 'ru',
    'locale': 'RU',
    'noReset': False,
    'autoAcceptAlerts': True
}
capabilities_android = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    "appPackage": "ru.berizaryad.android.staging",
    "appActivity": "ru.berizaryad.android.presentation.main.DrawerMainActivity",
    'language': 'ru',
    'noReset': False,
    'locale': 'RU',
    'autoGrantPermissions': True
}

appium_server_url = 'http://localhost:4723'


@pytest.fixture()
def driver_android():
    app_driver = webdriver.Remote(
        appium_server_url,
        options=UiAutomator2Options().load_capabilities(capabilities_android)
    )
    yield app_driver
    if app_driver.session_id:
        app_driver.quit()


@pytest.fixture()
def driver_ios():
    app_driver = webdriver.Remote(
        appium_server_url,
        options=XCUITestOptions().load_capabilities(capabilities_ios)
    )
    yield app_driver
    if app_driver.session_id:
        app_driver.quit()

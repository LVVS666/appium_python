import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

capabilities_android = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    "appPackage": "ru.berizaryad.android.dev3",
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

import time

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.android.settings',#открывает приложение settings
    appActivity='.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'


@pytest.fixture()
def driver():
        app_driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        yield app_driver
        if driver:
            app_driver.quit()


def test_find_battery(driver) -> None:
        el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')# ищет батарею
        el.click()
        time.sleep(5)


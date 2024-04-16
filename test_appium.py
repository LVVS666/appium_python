import time

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


capabilities = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    "appPackage": "ru.berizaryad.android.dev2",
    "appActivity": "ru.berizaryad.android.presentation.main.DrawerMainActivity",
    'language': 'en',
    'locale': 'US'
}


appium_server_url = 'http://localhost:4723'


@pytest.fixture()
def driver():
        app_driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        yield app_driver
        if driver:
            app_driver.quit()


def test_find_battery(driver) -> None:
    element_wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH,
                                        "//android.view.ViewGroup[@resource-id='ru.berizaryad.android.dev2:id/phoneBtnInclusion']"))
    )
    element = driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@resource-id='ru.berizaryad.android.dev2:id/phoneBtnInclusion']")
    time.sleep(5)
    assert element, f'Элемент не найден'

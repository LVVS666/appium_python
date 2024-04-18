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
    "appPackage": "ru.berizaryad.android.staging",
    "appActivity": "ru.berizaryad.android.presentation.main.DrawerMainActivity",
    'language': 'en',
    'noReset': True,
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
    '''Заходим по телефону'''
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((AppiumBy.XPATH,
    #                                     "//android.view.ViewGroup[@resource-id='ru.berizaryad.android.staging:id/phoneBtnInclusion']"))
    # )
    # element = driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@resource-id='ru.berizaryad.android.staging:id/phoneBtnInclusion']")
    # element.click()
    '''Выбираем коды страны'''
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH,
                                        '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvInstruction"]'))
    )
    element = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvInstruction"]')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH,
                                        '//android.widget.EditText[@resource-id="ru.berizaryad.android.staging:id/text_input_country_prefix"]'))
    )
    element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="ru.berizaryad.android.staging:id/text_input_country_prefix"]')
    element.click()
    '''Выбираем Россию'''
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH,
                                        '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvItem" and @text="(+7) Russia"]'))
    )
    element = driver.find_element(AppiumBy.XPATH,
                                  '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvItem" and @text="(+7) Russia"]')
    element.click()
    '''Находим строку ввода номера'''
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH,
                                        '//android.widget.EditText[@resource-id="ru.berizaryad.android.staging:id/edPhone"]'))
    )
    element = driver.find_element(AppiumBy.XPATH,
                                  '//android.widget.EditText[@resource-id="ru.berizaryad.android.staging:id/edPhone"]')
    element.click()
    element.send_keys('9232769943')
    '''Подверждаем номер телефона'''
    element = driver.find_element(AppiumBy.XPATH,
                                  '//android.widget.Button[@resource-id="ru.berizaryad.android.staging:id/btnNext"]')
    element.click()
    '''Вводим код подтверждения'''
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH,
                                        '//android.widget.LinearLayout[@resource-id="ru.berizaryad.android.staging:id/codeInputView"]/android.view.ViewGroup'))
    )
    element = driver.find_element(AppiumBy.XPATH,
                                  '//android.widget.LinearLayout[@resource-id="ru.berizaryad.android.staging:id/codeInputView"]/android.view.ViewGroup')
    element.click()
    driver.press_keycode(7)
    driver.press_keycode(7)
    driver.press_keycode(7)
    driver.press_keycode(8)
    assert WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH,
                                        '//android.widget.RelativeLayout[@resource-id="ru.berizaryad.android.staging:id/mapView"]/android.view.View'))
    ), f'Авторизация не произошла'

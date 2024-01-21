import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://mail.ru/'
browser = webdriver.Chrome()
browser.get(url=url)

try:
    '''Открыть сайт, найти кнопку создать почту, нажать кнопку.'''
    button_register = browser.find_element(By.LINK_TEXT, 'Создать почту')
    button_register.click()

finally:
    time.sleep(5)
    browser.quit()
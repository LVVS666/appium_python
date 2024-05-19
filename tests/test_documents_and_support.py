from element_locators import auth_elements as el
from page.android_app import AndroidApp


def test_list_country_in_doc(driver_android):
    '''Проверка отображения содержимого раздела документов'''
    app_login = AndroidApp(driver_android)
    app_login.registration(code_phone=el.russian_code, country=el.russia, phone=el.rus_kz_phone)
    app_login.documents()
    app_login.delete_user()


def test_all_doc_in_russia():
    pass


def test_all_doc_in_belarussia():
    pass


def test_all_doc_in_kirgistan():
    pass


def test_all_doc_in_kazahstan():
    pass


def test_support():
    pass



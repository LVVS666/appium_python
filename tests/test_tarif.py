from page.android_app import AndroidApp
from element_locators import auth_elements as el_auth, tariff_elements as el_tariff


def test_tariff_russia(driver_android):
    '''Проверка тарифа у России'''
    app_login = AndroidApp(driver_android)
    app_login.registration(code_phone=el_auth.russian_code, country=el_auth.russia, phone=el_auth.rus_kz_phone)
    app_login.tarif(tariff_country=el_tariff.russian_tariff, assert_text=el_tariff.assert_russian_tariff)
    app_login.delete_user()


def test_tariff_kazahstan(driver_android):
    '''Проверка тарифа у Казахстана'''
    app_login = AndroidApp(driver_android)
    app_login.registration(code_phone=el_auth.kazahstan_code, country=el_auth.kazahstan, phone=el_auth.rus_kz_phone)
    app_login.tarif(tariff_country=el_tariff.kazahstan_tariff, assert_text=el_tariff.assert_kazahstan_tariff)
    app_login.delete_user()


def test_tariff_kirgistan(driver_android):
    '''Проверка тарифа у Киргизии'''
    app_login = AndroidApp(driver_android)
    app_login.registration(code_phone=el_auth.kirgistan_code, country=el_auth.kirgistan, phone=el_auth.bld_kgz_phone)
    app_login.tarif(tariff_country=el_tariff.kirgistan_tariff, assert_text=el_tariff.assert_kirgistan_tariff)
    app_login.delete_user()


def test_tariff_belarussia(driver_android):
    '''Проверка тарифа у Беларуси'''
    app_login = AndroidApp(driver_android)
    app_login.registration(code_phone=el_auth.belarussia_code, country=el_auth.belarussia, phone=el_auth.bld_kgz_phone)
    app_login.tarif(tariff_country=el_tariff.belarussia_tariff, assert_text=el_tariff.assert_belarussia_tariff)
    app_login.delete_user()

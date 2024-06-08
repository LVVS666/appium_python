from page.android_app import AndroidApp
from element_locators import auth_elements as el_auth


def test_pay_subscription_in_main(driver_android):
    '''Покупка подписки с главного экрана, проверка счетчика на главном экране и в разделе подписки'''
    app_login = AndroidApp(driver_android)
    app_login.registration(code_phone=el_auth.russian_code, country=el_auth.russia, phone=el_auth.rus_kz_phone)
    app_login.add_card_in_russia()
    app_login.pay_subscription_on_map()
    app_login.delete_user()
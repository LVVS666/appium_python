# from element_locators import auth_elements as el_auth
# from page.subscriptions import Subscriptions


# def test_pay_subscription_in_main(driver_android):
#     '''Покупка подписки с главного экрана, проверка счетчика на главном экране и в разделе подписки'''
#     app_login = Subscriptions(driver_android)
#     app_login.registration(code_phone=el_auth.russian_code, country=el_auth.russia, phone=el_auth.rus_kz_phone)
#     app_login.add_card_in_russia()
#     app_login.pay_subscription_on_map()
#     app_login.delete_user()
#
#
# def test_pay_subscription_and_off(driver_android):
#     '''Покупка подписки на главном экране, отказ от автопродление, автопродление'''
#     app_login = Subscriptions(driver_android)
#     app_login.registration(code_phone=el_auth.russian_code, country=el_auth.russia, phone=el_auth.rus_kz_phone)
#     app_login.add_card_in_russia()
#     app_login.pay_subscription_on_and_off()
#     app_login.delete_user()
#
#
# def test_pay_subscription_in_banner(driver_android):
#     '''Покупка подписки с через баннер после привязки карты, проверка счетчика на главном экране,в разделе подписки, в меню'''
#     app_login = Subscriptions(driver_android)
#     app_login.registration(code_phone=el_auth.russian_code, country=el_auth.russia, phone=el_auth.rus_kz_phone)
#     app_login.pay_subscription_on_banner()
#     app_login.delete_user()
#
#
# def test_pay_subscription_on_menu(driver_android):
#     '''Покупка подписки в меню, проверка счетчика на главном экране,в разделе подписки, в меню'''
#     app_login = Subscriptions(driver_android)
#     app_login.registration(code_phone=el_auth.russian_code, country=el_auth.russia, phone=el_auth.rus_kz_phone)
#     app_login.add_card_in_russia()
#     app_login.pay_subscription_on_menu()
#     app_login.delete_user()

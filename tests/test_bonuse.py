from element_locators import bonuse_elements as el_bonuse
from element_locators import auth_elements as el_auth
from page.bonuse import Bonuse


def test_add_bonuse_in_new_user(driver_android):
    '''Ввести промокод для нового юзера, проверить начисление бонусов, повторно ввести промокод'''
    app_login = Bonuse(driver_android)
    app_login.registration(
        code_phone=el_auth.russian_code,
        country=el_auth.russia,
        phone=el_auth.rus_kz_phone,
    )
    app_login.open_bonuse()
    app_login.new_user_promocode()
    app_login.exit_map_bonus_count_in_menu('100')
    app_login.click_element(el_bonuse.bonuse_menu_button)
    app_login.repeat_new_user_promocode()
    app_login.delete_user()


def test_add_bonuse_in_old_user(driver_android):
    '''Ввести промокод для старого юзера, проверить наличие бонусов, ввести повторно промокод'''
    app_login = Bonuse(driver_android)
    app_login.registration(
        code_phone=el_auth.russian_code,
        country=el_auth.russia,
        phone=el_auth.rus_kz_phone,
    )
    app_login.open_bonuse()
    app_login.old_user_promocode()
    app_login.exit_map_bonus_count_in_menu('100')
    app_login.click_element(el_bonuse.bonuse_menu_button)
    app_login.repeat_old_user_promocode()
    app_login.delete_user()


def test_add_bonuse_new_user_promocode_in_old_user(driver_android):
    '''Ввести промокод для нового юзера, старым юзером'''
    app_login = Bonuse(driver_android)
    app_login.registration(
        code_phone=el_auth.russian_code,
        country=el_auth.russia,
        phone=el_auth.rus_kz_phone,
    )
    app_login.open_bonuse()
    app_login.new_promocode_old_user()
    app_login.delete_user()


def test_send_expiry_promocode_and_count_0_promocode(driver_android):
    '''Ввод протухшего промокода и промокода с количеством использований = 0'''
    app_login = Bonuse(driver_android)
    app_login.registration(
        code_phone=el_auth.russian_code,
        country=el_auth.russia,
        phone=el_auth.rus_kz_phone,
    )
    app_login.open_bonuse()
    app_login.expiry_promocode()
    app_login.count_0_promocode()
    app_login.delete_user()


def test_add_bonuse_company_promocode_new_user(driver_android):
    '''Ввод промокода компании новым юзером'''
    app_login = Bonuse(driver_android)
    app_login.registration(
        code_phone=el_auth.russian_code,
        country=el_auth.russia,
        phone=el_auth.rus_kz_phone,
    )
    app_login.open_bonuse()
    app_login.company_promocode()
    app_login.exit_map_bonus_count_in_menu('100')
    app_login.delete_user()


def test_send_not_validate_promocode_in_new_user(driver_android):
    '''Ввод несуществующего промокода новым юзером'''
    app_login = Bonuse(driver_android)
    app_login.registration(
        code_phone=el_auth.russian_code,
        country=el_auth.russia,
        phone=el_auth.rus_kz_phone,
    )
    app_login.open_bonuse()
    app_login.not_validate_promocode()
    app_login.delete_user()


def test_send_not_validate_promocode_in_old_user(driver_android):
    '''Ввод несуществующего промокода старым юзером'''
    app_login = Bonuse(driver_android)
    app_login.registration(
        code_phone=el_auth.russian_code,
        country=el_auth.russia,
        phone=el_auth.rus_kz_phone,
    )
    app_login.open_bonuse()
    app_login.not_validate_promocode()
    app_login.delete_user()

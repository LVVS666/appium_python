from element_locators import bonuse_elements as el_bonus
from page.auth import Auth


class Bonuse(Auth):
    '''Класс бонусов'''
    def open_bonuse(self):
        '''Открытие раздела бонусов'''
        self.click_element(el_bonus.main_menu)
        self.click_element(el_bonus.bonuse_menu_button)
    def send_promocode(self, promocode):
        '''Взаимодействие с формой ввода промокода'''
        self.click_element(el_bonus.enter_promocode_button)
        self.send_keys_element(el_bonus.form_promocode, promocode)
        self.click_element(el_bonus.send_promocode)

    def new_user_promocode(self):
        '''Промокод для нового юзера'''
        self.send_promocode(el_bonus.new_user_promocode)
        self.wait(el_bonus.success_promocode)
        self.wait(el_bonus.bunuse_count)
        count = self.find(el_bonus.bunuse_count)
        assert count.text == 100, 'Количество бонусов не соответствует'

    def repeat_new_user_promocode(self):
        '''Повторный ввод промокода для нового юзера'''
        self.send_promocode(el_bonus.new_user_promocode)
        self.wait(el_bonus.not_activate_promocode)

    def new_promocode_old_user(self):
        '''Ввод промокода для нового юзера старым юзером'''
        self.send_promocode(el_bonus.new_user_promocode)
        self.wait(el_bonus.not_activate_promocode)

    def old_user_promocode(self):
        '''Ввод промокода для старого юзера'''
        self.send_promocode(el_bonus.old_user_promocode)
        self.wait(el_bonus.success_promocode)
        self.wait(el_bonus.not_activate_promocode)
        self.wait(el_bonus.bunuse_count)
        count = self.find(el_bonus.bunuse_count)
        assert count.text == 200, 'Количество бонусов не соответствует'

    def repeat_old_user_promocode(self):
        '''Повторный ввод промокода для старого юзера'''
        self.send_promocode(el_bonus.old_user_promocode)
        self.wait(el_bonus.not_activate_promocode)

    def company_promocode(self):
        self.wait(el_bonus.bunuse_count)
        count = self.find(el_bonus.bunuse_count)
        assert count.text == 300, 'Количество бонусов не соответствует'
        pass

    def expiry_promocode(self):
        '''Ввод протухшего промокода'''
        self.send_promocode(el_bonus.expiry_promocode)
        self.wait(el_bonus.not_work_promocode)

    def count_0_promocode(self):
        '''Ввод промокода с количеством использований = 0'''
        self.send_promocode(el_bonus.count_0_promocode)
        self.wait(el_bonus.not_work_promocode)

    def exit_map_bonus_count_in_menu(self, bonuse):
        '''Проверка отображения количества бонусов в меню'''
        self.click_element(el_bonus.main_menu)
        self.click_element(el_bonus.main_menu)
        self.wait(el_bonus.bonuse_count_menu)
        count = self.find(el_bonus.bonuse_count_menu)
        assert count.text == bonuse, 'Количество бонусов в меню не соответствует'

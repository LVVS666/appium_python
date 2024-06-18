from appium.webdriver.common.appiumby import AppiumBy

# Номера телефонов
rus_kz_phone = '9992769943'
bld_kgz_phone = '255108000'

# Кнопки
login_in_phone = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'phoneBtnInclusion')]"
)
button_send_phone = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'btnNext')]"
)
on_delete = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'btnConfirm')]"
)
complete_delete_button = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'btnOk')]"
)

# Текст
page_send_phone = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'tvInstruction')]"
)
russian_code = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'tvItem') and @text='(+7) Россия']"
)
belarussia_code = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'tvItem') and @text='(+375) Беларусь']"
)
kazahstan_code = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'tvItem') and @text='(+7) Казахстан']"
)
kirgistan_code = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'tvItem') and @text='(+996) Киргизия']"
)
profile_user = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'menuText') and @text='Профиль']"
)
delete_user = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'title') and @text='Удалить аккаунт']"
)
button_exit = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'title') and @text='Выйти']"
)

# Ввести текст
code_country = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'text_input_country_prefix')]"
)
search_country = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'etSearch')]"
)
form_phone = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'edPhone')]"
)

# Чекбоксы
russia = (
    AppiumBy.XPATH,
    "(//*[ends-with(@resource-id, 'checkBox')])[1]"
)
belarussia = (
    AppiumBy.XPATH,
    "(//*[ends-with(@resource-id, 'checkBox')])[2]"
)
kazahstan = (
    AppiumBy.XPATH,
    "(//*[ends-with(@resource-id, 'checkBox')])[3]"
)
kirgistan = (
    AppiumBy.XPATH,
    "(//*[ends-with(@resource-id, 'checkBox')])[4]"
)

# Вьюхи
code_input = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'codeInputView')]/android.view.ViewGroup"
)
main_map = (
    AppiumBy.XPATH,
    "//android.view.View"
)
outside_map = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'touch_outside')]"
)

# Меню
main_menu = (
    AppiumBy.XPATH,
    "//*[@content-desc='Открыть навигацию']"
)
exit_and_delete = (
    AppiumBy.XPATH,
    "//*[@content-desc='Ещё']"
)

# Подписка и бонусы
subscription = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'btSub')]/android.view.ViewGroup"
)
bonuse = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'btBonus')]/android.view.ViewGroup"
)

# Выбор страны
button_send_country = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'btnSelect')]"
)

# Зоны
RUS_SBER = "RUS_SBER"
KZ_CHARGE = "KZ_CHARGE"
KGZ = "KGZ"
BLR_BEPAID = "BLR_BEPAID"

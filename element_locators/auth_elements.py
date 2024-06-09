from appium.webdriver.common.appiumby import AppiumBy

rus_kz_phone = '9992769943'
bld_kgz_phone = '255108000'

login_in_phone = (
    AppiumBy.XPATH,
    "//android.view.ViewGroup[@resource-id='ru.berizaryad.android.staging:id/phoneBtnInclusion']"
    )

page_send_phone = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvInstruction"]'
    )

code_country = (
    AppiumBy.XPATH,
    '//android.widget.EditText[@resource-id="ru.berizaryad.android.staging:id/text_input_country_prefix"]'
    )

search_country = (
    AppiumBy.XPATH,
    '//android.widget.EditText[@resource-id="ru.berizaryad.android.staging:id/etSearch"]'
)

russian_code = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvItem" and @text="(+7) Россия"]'
    )

belarussia_code = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvItem" and @text="(+375) Беларусь"]'
)

kazahstan_code = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvItem" and @text="(+7) Казахстан"]'
)

kirgistan_code = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvItem" and @text="(+996) Киргизия"]'
)

form_phone = (
    AppiumBy.XPATH,
    '//android.widget.EditText[@resource-id="ru.berizaryad.android.staging:id/edPhone"]'
    )

button_send_phone = (
    AppiumBy.XPATH,
    '//android.widget.Button[@resource-id="ru.berizaryad.android.staging:id/btnNext"]'
    )

code_input = (
    AppiumBy.XPATH,
    '//android.widget.LinearLayout[@resource-id="ru.berizaryad.android.staging:id/codeInputView"]/android.view.ViewGroup'
    )

main_map = (
    AppiumBy.XPATH,
    '//android.view.View'
    )

russia = (
    AppiumBy.XPATH,
    '(//android.widget.CheckBox[@resource-id="ru.berizaryad.android.staging:id/checkBox"])[1]'
    )

belarussia = (
    AppiumBy.XPATH,
    '(//android.widget.CheckBox[@resource-id="ru.berizaryad.android.staging:id/checkBox"])[2]'
    )

kazahstan = (
    AppiumBy.XPATH,
    '(//android.widget.CheckBox[@resource-id="ru.berizaryad.android.staging:id/checkBox"])[3]'
    )

kirgistan = (
    AppiumBy.XPATH,
    '(//android.widget.CheckBox[@resource-id="ru.berizaryad.android.staging:id/checkBox"])[4]'
    )

button_send_country = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/btnSelect"]'
)

subscription = (
    AppiumBy.XPATH,
    '//android.widget.FrameLayout[@resource-id="ru.berizaryad.android.staging:id/btSub"]/android.view.ViewGroup'
)

bonuse = (
    AppiumBy.XPATH,
    '//android.widget.FrameLayout[@resource-id="ru.berizaryad.android.staging:id/btBonus"]/android.view.ViewGroup'
)

main_menu = (
    AppiumBy.XPATH,
    '//android.widget.ImageButton[@content-desc="Открыть навигацию"]'
    )

profile_user = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/menuText" and @text="Профиль"]'
    )

exit_and_delete = (
    AppiumBy.XPATH,
    '//android.widget.ImageView[@content-desc="Ещё"]'
    )

delete_user = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/title" and @text="Удалить аккаунт"]'
    )

on_delete = (
    AppiumBy.XPATH,
    '//android.widget.Button[@resource-id="ru.berizaryad.android.staging:id/btnConfirm"]'
    )

button_exit = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/title" and @text="Выйти"]'
)

outside_map = (
    AppiumBy.XPATH,
    '//android.view.View[@resource-id="ru.berizaryad.android.staging:id/touch_outside"]'
)

complete_delete_button = (
    AppiumBy.XPATH,
    '//android.widget.Button[@resource-id="ru.berizaryad.android.staging:id/btnOk"]'
)

'''Зоны'''
RUS_SBER = "RUS_SBER"
KZ_CHARGE = "KZ_CHARGE"
KGZ = "KGZ"
BLR_BEPAID = "BLR_BEPAID"

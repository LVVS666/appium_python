from appium.webdriver.common.appiumby import AppiumBy


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

russian_code = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvItem" and @text="(+7) Russia"]'
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
    '//android.widget.RelativeLayout[@resource-id="ru.berizaryad.android.staging:id/mapView"]/android.view.View'
    )

russia = (
    AppiumBy.XPATH,
    '(//androidx.cardview.widget.CardView[@resource-id="ru.berizaryad.android.staging:id/root"])[1]/android.view.ViewGroup'
    )

belarussia = (
    AppiumBy.XPATH,
    '(//androidx.cardview.widget.CardView[@resource-id="ru.berizaryad.android.staging:id/root"])[2]/android.view.ViewGroup'
    )

kazahstan = (
    AppiumBy.XPATH,
    '(//androidx.cardview.widget.CardView[@resource-id="ru.berizaryad.android.staging:id/root"])[3]/android.view.ViewGroup'
    )

kirgistan = (
    AppiumBy.XPATH,
    '(//androidx.cardview.widget.CardView[@resource-id="ru.berizaryad.android.staging:id/root"])[4]/android.view.ViewGroup'
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
    '//android.widget.ImageView[@content-desc="Другие параметры"]'
    )

delete_user = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/title" and @text="Удалить аккаунт"]'
    )

on_delete = (
    AppiumBy.XPATH,
    '//android.widget.Button[@resource-id="ru.berizaryad.android.staging:id/btnConfirm"]'
    )
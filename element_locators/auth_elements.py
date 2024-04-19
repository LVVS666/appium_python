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

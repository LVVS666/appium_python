from appium.webdriver.common.appiumby import AppiumBy

main_button_card = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/title"]'
)
user_cards = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/menuText" and @text="Способ оплаты"]'
)
back_to_map = (
    AppiumBy.XPATH,
    '//android.widget.ImageButton[@content-desc="Открыть навигацию"]'
)
bin_card = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvCardNumber"]'
)
banner_off = (
    AppiumBy.XPATH,
    '//android.widget.ImageView[@resource-id="ru.berizaryad.android.staging:id/closeImageView"]'
)
banner_card_ok = (
    AppiumBy.XPATH,
    '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.LinearLayout'
)


'''Данные для России'''
form_number_card_in_russia = (
    AppiumBy.XPATH,
    '//android.webkit.WebView[@text="Страница оплаты"]/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[3]/android.view.View/android.view.View/android.widget.EditText'
)
number_russia = '2201382000000013'
form_year_card_in_russia = (
    AppiumBy.XPATH,
    '//android.webkit.WebView[@text="Страница оплаты"]/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[4]/android.view.View/android.view.View/android.widget.EditText'
)
year_russia = '1224'
form_cvc_in_russia = (
    AppiumBy.XPATH,
    '//android.webkit.WebView[@text="Страница оплаты"]/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[5]/android.view.View/android.view.View/android.widget.EditText'
)
cvc_russia = '123'
button_pay_in_russia = (
    AppiumBy.XPATH,
    '//android.widget.Button[@text="Оплатить"]'
)
operation_button_ok_in_russia = (
    AppiumBy.XPATH,
    '//android.widget.Button[@text="Success"]'
)
bin_russia = '**** 0013'


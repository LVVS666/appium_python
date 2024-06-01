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
add_card = (
    AppiumBy.XPATH,
    '//android.widget.Button[@resource-id="ru.berizaryad.android.staging:id/btChange"]'
)
subscription_add = (
    AppiumBy.XPATH,
    '//android.widget.LinearLayout[@resource-id="ru.berizaryad.android.staging:id/btActivate"]'
)
subscription_ok = (
    AppiumBy.XPATH,
    '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.LinearLayout'
)

replace_new_card = (
    AppiumBy.XPATH,
    '//android.widget.Button[@text="Оплатить новой картой"]'
)


'''Данные для России'''
form_number_card_in_russia = (
    AppiumBy.XPATH,
    '//android.webkit.WebView[@text="Страница оплаты"]/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[3]/android.view.View/android.view.View/android.widget.EditText'
    ''
)
new_form_number_card_in_russia = (
    AppiumBy.XPATH,
    '//android.webkit.WebView[@text="Страница оплаты"]/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.view.View[3]/android.view.View/android.view.View/android.widget.EditText'
)
number_russia = '2201382000000013'
new_number_russia = '2201382000000054'
form_year_card_in_russia = (
    AppiumBy.XPATH,
    '//android.webkit.WebView[@text="Страница оплаты"]/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[4]/android.view.View/android.view.View/android.widget.EditText'
)
new_form_year_card_in_russia = (
    AppiumBy.XPATH,
    '//android.webkit.WebView[@text="Страница оплаты"]/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.view.View[4]/android.view.View/android.view.View/android.widget.EditText'
)
year_russia = '1224'
form_cvc_in_russia = (
    AppiumBy.XPATH,
    '//android.webkit.WebView[@text="Страница оплаты"]/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[5]/android.view.View/android.view.View/android.widget.EditText'
)
new_form_cvc_in_russia = (
    AppiumBy.XPATH,
    '//android.webkit.WebView[@text="Страница оплаты"]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[5]/android.view.View/android.view.View/android.widget.EditText'

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
new_bin_russia = '**** 0054'


'''Данные для Беларуси'''

form_number_card_in_belarussia = (
    AppiumBy.XPATH,
    '//android.view.View[@text="BePaidWidget"]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.EditText'
)
number_belarussia = '4200000000000000'
form_year_card_in_belarussia = (
    AppiumBy.XPATH,
    '//android.view.View[@text="BePaidWidget"]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText'
)
year_belarussia = '1224'
form_cvc_in_belarussia = (
    AppiumBy.XPATH,
    '//android.view.View[@text="BePaidWidget"]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[1]/android.widget.EditText'
)
cvc_belarussia = '123'
button_pay_in_belarussia = (
    AppiumBy.XPATH,
    '//android.widget.Button[@text="Pay 4.00 BYN"]'
)
operation_button_ok_in_belarussia = (
    AppiumBy.XPATH,
    '//android.widget.Button[@text="Continue"]'
)
bin_belarussia = '**** 0000'



'''Данные для Казахстана '''
form_number_card_in_kazahstan = (
    AppiumBy.XPATH,
    '//android.widget.EditText[@resource-id="ru.berizaryad.android.staging:id/edCardNumber"]'
)
number_kazahstan = '4242424242424242'
new_number_kazahstan = '5555555555554444'
form_year_card_in_kazahstan = (
    AppiumBy.XPATH,
    '//android.widget.EditText[@resource-id="ru.berizaryad.android.staging:id/edCardDate"]'
)
year_kazahstan = '1224'
form_cvc_in_kazahstan = (
    AppiumBy.XPATH,
    '//android.widget.EditText[@resource-id="ru.berizaryad.android.staging:id/edCardCvv"]'
)
cvc_kazahstan = '123'
button_pay_in_kazahstan = (
    AppiumBy.XPATH,
    '//android.widget.Button[@resource-id="ru.berizaryad.android.staging:id/btChargeOrder"]'
)
operation_button_ok_in_kazahstan = (
    AppiumBy.XPATH,
    '//android.widget.Button[@text="Успех"]'
)
bin_kazahstan = '**** 4242'
new_bin_kazahstan = '**** 4444'


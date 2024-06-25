from appium.webdriver.common.appiumby import AppiumBy

sbp_button = (
    AppiumBy.XPATH,
    '//android.widget.ImageButton[@resource-id="ru.berizaryad.android.dev2:id/btSbp"]'
)

sberpay_button = (
    AppiumBy.XPATH,
    '//android.widget.ImageButton[@resource-id="ru.berizaryad.android.dev2:id/btSberPay"]'
)

card_button = (
    AppiumBy.XPATH,
    '//android.widget.Button[@resource-id="ru.berizaryad.android.dev2:id/btBankCard"]'
)

off_banner_card = (
    AppiumBy.XPATH,
    '//android.widget.ImageButton[@content-desc="Закрыть"]'
)

main_button_card = (
    AppiumBy.XPATH,
    '//android.widget.FrameLayout[@resource-id="ru.berizaryad.android.dev2:id/btTakePowerBank"]/android.widget.LinearLayout'
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
    '//android.webkit.WebView[@text="Страница оплаты"]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View/android.view.View/android.widget.EditText'
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
new_number_belarussia = '4012000000001055'
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
new_bin_belarussia = '**** 1055'


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


'''Данные для Киргизии'''
form_number_card_in_kirgistan = (
    AppiumBy.XPATH,
    '//android.webkit.WebView[@text="Оплата"]/android.view.View/android.view.View/android.view.View[4]/android.view.View[1]/android.widget.EditText'
)
number_kirgistan = '4706 3937 0789 1337.'
new_number_kirgistan = '4478 1900 2339 9995'
form_year_card_in_kirgistan_month = (
    AppiumBy.XPATH,
    '//android.webkit.WebView[@text="Оплата"]/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.EditText'
)
year_kirgistan_month = '09'
accec_09 = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="09"]'
)
new_year_kirgistan_month = '05'
accec_05 = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="05"]'
)
form_year_card_in_kirgistan_year = (
    AppiumBy.XPATH,
    '//android.webkit.WebView[@text="Оплата"]/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.EditText'
)
year_kirgistan_year = '2026'
accec_2026 = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="2026"]'
)
new_year_kirgistan_year = '2027'
accec_2027 = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="2027"]'
)
form_cvc_in_kirgistan = (
    AppiumBy.XPATH,
    '//android.webkit.WebView[@text="Оплата"]/android.view.View/android.view.View[1]/android.view.View[4]/android.view.View[4]/android.widget.EditText'
)
cvc_kirgistan = '544'
new_cvc_kirgistan = '840'
click_window = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="Номер заказа №"]'
)
button_pay_in_kirgistan = (
    AppiumBy.XPATH,
    '//android.widget.Button[@text="Оплатить 1.00 KGS"]'
)

bin_kirgistan = '**** 1337'
new_bin_kirgistan = '**** 9995'

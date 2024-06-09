from appium.webdriver.common.appiumby import AppiumBy

banner_subscription_pay = (
    AppiumBy.XPATH,
    '//android.widget.Button[@resource-id="ru.berizaryad.android.staging:id/btnNavSubscription"]'
)


how_in_work_subscription = (
    AppiumBy.XPATH,
    '//android.widget.Button[@resource-id="ru.berizaryad.android.staging:id/btHowItWork"]'
)
banner_how_in_work = (
    AppiumBy.XPATH,
    '//android.webkit.WebView[@text="Как работает подписка Бери Заряд"]/android.view.View/android.view.View[1]/android.view.View/android.view.View'
)
access_banner = 'Как работает подписка Бери Заряд'
count_subscription = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvRemainingCap"]'
)
access_count = '7/7'
count_dicsription_subscription = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/appCompatTextView24"]'
)
button_off_subscription = (
    AppiumBy.XPATH,
    '//android.widget.Button[@resource-id="ru.berizaryad.android.staging:id/btDelete"]'
)
on_delete = (
    AppiumBy.XPATH,
    '//android.widget.Button[@resource-id="ru.berizaryad.android.staging:id/button_negative"]'
)
subscription_off_text = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvDescription"]'
)
access_text = 'Автопродление отключено'
button_return_subscription = (
    AppiumBy.XPATH,
    '//android.widget.Button[@resource-id="ru.berizaryad.android.staging:id/btActivate"]'
)
off_subscription = (
    AppiumBy.XPATH,
    '//android.widget.ImageView[@resource-id="ru.berizaryad.android.staging:id/imgRight"]'
)


subscriptions = (
    AppiumBy.XPATH,
    '//android.widget.FrameLayout[@resource-id="ru.berizaryad.android.staging:id/btSub"]/android.view.ViewGroup'
)
button_subscription = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvSubSecond"]'
)
access_button = '7 АРЕНД'


count_subscription_button = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvSubscriptionTitle"]'
)
back_map = (
    AppiumBy.XPATH,
    '//android.widget.ImageButton[@resource-id="ru.berizaryad.android.staging:id/ivMinus"]'
)

subscriptions_menu = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/menuText" and @text="Подписка"]'
)
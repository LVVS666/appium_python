from appium.webdriver.common.appiumby import AppiumBy

# Баннер подписки и оплаты
banner_subscription_pay = (
    AppiumBy.XPATH,
    '//android.widget.Button[contains(@resource-id, "btnNavSubscription")]'
)

# Как работает подписка
how_in_work_subscription = (
    AppiumBy.XPATH,
    '//android.widget.Button[contains(@resource-id, "btHowItWork")]'
)
banner_how_in_work = (
    AppiumBy.XPATH,
    '//android.webkit.WebView[@text="Как работает подписка Бери Заряд"]/android.view.View/android.view.View[1]/android.view.View/android.view.View'
)
access_banner = 'Как работает подписка Бери Заряд'
count_subscription = (
    AppiumBy.XPATH,
    '//android.widget.TextView[contains(@resource-id, "tvRemainingCap")]'
)
access_count = '7/7'
count_dicsription_subscription = (
    AppiumBy.XPATH,
    '//android.widget.TextView[contains(@resource-id, "appCompatTextView24")]'
)
button_off_subscription = (
    AppiumBy.XPATH,
    '//android.widget.Button[contains(@resource-id, "btDelete")]'
)
on_delete = (
    AppiumBy.XPATH,
    '//android.widget.Button[contains(@resource-id, "button_negative")]'
)
subscription_off_text = (
    AppiumBy.XPATH,
    '//android.widget.TextView[contains(@resource-id, "tvDescription")]'
)
access_text = 'Автопродление отключено'
button_return_subscription = (
    AppiumBy.XPATH,
    '//android.widget.Button[contains(@resource-id, "btActivate")]'
)
off_subscription = (
    AppiumBy.XPATH,
    '//android.widget.ImageView[contains(@resource-id, "imgRight")]'
)

# Подписки
subscriptions = (
    AppiumBy.XPATH,
    '//android.widget.FrameLayout[contains(@resource-id, "btSub")]/android.view.ViewGroup'
)
button_subscription = (
    AppiumBy.XPATH,
    '//android.widget.TextView[contains(@resource-id, "tvSubSecond")]'
)
access_button = '7 АРЕНД'

count_subscription_button = (
    AppiumBy.XPATH,
    '//android.widget.TextView[contains(@resource-id, "tvSubscriptionTitle")]'
)
back_map = (
    AppiumBy.XPATH,
    '//android.widget.ImageButton[contains(@resource-id, "ivMinus")]'
)

subscriptions_menu = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="Подписка"]'
)

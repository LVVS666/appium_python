from appium.webdriver.common.appiumby import AppiumBy

tariff_menu = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/menuText" and @text="Тарифы"]'
)

tariff_close = (
    AppiumBy.XPATH,
    '//android.widget.ImageButton[@content-desc="Открыть навигацию"]'
)

russian_tariff = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="Тестовый тариф для России со Сбер. (rus_sber)"]'
)
assert_russian_tariff = 'Тестовый тариф для России со Сбер. (rus_sber)'

kazahstan_tariff = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="KZ_CHARGE"]'
)
assert_kazahstan_tariff = 'KZ_CHARGE'

kirgistan_tariff = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="КГЗ"]'
)
assert_kirgistan_tariff = 'КГЗ'

belarussia_tariff = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="Тарифы для Беларуси"]'
)
assert_belarussia_tariff = 'Тарифы для Беларуси'
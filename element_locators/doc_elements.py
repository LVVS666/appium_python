from appium.webdriver.common.appiumby import AppiumBy


documents = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/menuText" and @text="Документы"]'
)

russian_documents = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvCountryName" and @text="Российская Федерация"]'
)

kazahstan_documents = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvCountryName" and @text="Казахстан"]'
)

kirgistan_documents = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvCountryName" and @text="Кыргызстан"]'
)

belarussia_documents = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvCountryName" and @text="Беларусь"]'
)

button_back_documents = (
    AppiumBy.XPATH,
    '//android.widget.ImageButton[@resource-id="ru.berizaryad.android.staging:id/btnBack"]'
)

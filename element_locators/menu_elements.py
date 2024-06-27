from appium.webdriver.common.appiumby import AppiumBy

main_menu = (
    AppiumBy.XPATH,
    '//android.widget.ImageButton[@content-desc="Открыть навигацию"]'
)
out_back_map = (
    AppiumBy.XPATH,
    '//android.view.View[@resource-id="ru.berizaryad.android.staging:id/touch_outside"]'
)
back = (
    AppiumBy.XPATH,
    '//android.widget.ImageButton'
)


# Неавторизованный пользователь
auth = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/menuText" and @text="Войти"]'
)
auth_access = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvChooseTitle"]'
)
text_auth = 'Выберете способ верификации'
# закрывается out_back_map


support = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/menuText" and @text="Поддержка"]'
)
support_content = (
    AppiumBy.XPATH,
    '(//android.widget.LinearLayout[@resource-id="ru.berizaryad.android.staging:id/layoutContent"])[1]'
)
# закрывается out_back_map


documents = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/menuText" and @text="Документы"]'
)
doc_access = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvTitle"]'
)
text_doc = 'Выбери страну'
back_documents = (
    AppiumBy.XPATH,
    '//android.widget.ImageButton[@resource-id="ru.berizaryad.android.staging:id/btnBack"]'
)


franchizing = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/menuText" and @text="Франчайзинг"]'
)
main_banner = (
    AppiumBy.XPATH,
    '//android.view.ViewGroup[@resource-id="ru.berizaryad.android.staging:id/clMainModal"]'
)
# раздел франшизы использует для закрытия локатор бокового меню

about = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/menuText" and @text="О приложении"]'
)
about_content = (
    AppiumBy.XPATH,
    '//android.widget.FrameLayout[@resource-id="ru.berizaryad.android.staging:id/container"]/android.widget.LinearLayout/android.view.ViewGroup'
)
# использует локатор back для возврата

# Авторизованный пользователь
profile = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/menuText" and @text="Профиль"]'
)
profile_content = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvPhoneTitle"]'
)
# использует локатор back для возврата


pay = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/menuText" and @text="Способ оплаты"]'
)
pay_content = (
    AppiumBy.XPATH,
    '//android.widget.LinearLayout[@resource-id="ru.berizaryad.android.staging:id/llCard"]'
)
# использует для закрытия локатор бокового меню


subsctiption = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/menuText" and @text="Подписка"]'
)


partners = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/menuText" and @text="Акции партнеров"]'
)
partners_content = (
    AppiumBy.XPATH,
    '//androidx.recyclerview.widget.RecyclerView[@resource-id="ru.berizaryad.android.staging:id/recyclerViewPartners"]'
)
# использует для закрытия локатор бокового меню


tariff = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/menuText" and @text="Тарифы"]'
)
tariff_content = (
    AppiumBy.XPATH,
    '//android.view.ViewGroup[@resource-id="ru.berizaryad.android.staging:id/clMainModal"]/android.webkit.WebView/android.webkit.WebView'
)
# использует для закрытия локатор бокового меню


bonuse = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/menuText" and @text="Бонусы"]'
)
bonus_access = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvShare"]'
)
text_bonus = 'Делись бонусами и заряжайся бесплатно'
# использует для закрытия локатор бокового меню

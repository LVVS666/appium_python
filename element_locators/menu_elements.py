from appium.webdriver.common.appiumby import AppiumBy

# Основное меню
main_menu = (
    AppiumBy.XPATH,
    '//android.widget.ImageButton[@content-desc="Открыть навигацию"]'
)
out_back_map = (
    AppiumBy.XPATH,
    "//*[ends-with(@resource-id, 'touch_outside')]"
)
back = (
    AppiumBy.XPATH,
    '//android.widget.ImageButton'
)
document_back = (
    AppiumBy.ID,
    'ru.berizaryad.android.staging:id/btnBack'
)

# Неавторизованный пользователь
auth = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="Войти"]'
)
auth_access = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvChooseTitle"]'
)
text_auth = 'Выбери способ верификации'
# закрывается out_back_map

support = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="Поддержка"]'
)
support_content = (
    AppiumBy.XPATH,
    '(//android.widget.LinearLayout[contains(@resource-id, "layoutContent")])[1]'
)
# закрывается out_back_map

documents = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="Документы"]'
)
doc_access = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="Выбери страну"]'
)
text_doc = 'Выбери страну'
back_documents = (
    AppiumBy.XPATH,
    '//android.widget.ImageButton[@resource-id="ru.berizaryad.android.staging:id/btnBack"]'
)

franchizing = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="Франчайзинг"]'
)
main_banner = (
    AppiumBy.XPATH,
    '//android.view.ViewGroup[@resource-id="ru.berizaryad.android.staging:id/clMainModal"]'
)
# раздел франшизы использует для закрытия локатор бокового меню

about = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="О приложении"]'
)
about_content = (
    AppiumBy.XPATH,
    '//android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup'
)
# использует локатор back для возврата

# Авторизованный пользователь
profile = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="Профиль"]'
)
profile_content = (
    AppiumBy.XPATH,
    'ru.berizaryad.android.staging:id/tvPhoneValue'
)
# использует локатор back для возврата

pay = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="Способ оплаты"]'
)
pay_content = (
    AppiumBy.XPATH,
    '//android.widget.LinearLayout[contains(@resource-id, "llCard")]'
)
# использует для закрытия локатор бокового меню

subscription = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="Подписка"]'
)

partners = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="Акции партнеров"]'
)
partners_content = (
    AppiumBy.XPATH,
    '//androidx.recyclerview.widget.RecyclerView[@resource-id="ru.berizaryad.android.staging:id/recyclerViewPartners"]'
)
# использует для закрытия локатор бокового меню

tariff = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="Тарифы"]'
)
tariff_content = (
    AppiumBy.XPATH,
    '//android.webkit.WebView/android.webkit.WebView'
)
# использует для закрытия локатор бокового меню

bonuses = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="Бонусы"]'
)
bonus_access = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="Делись бонусами и заряжайся бесплатно"]'
)
text_bonus = 'Делись бонусами и заряжайся бесплатно'
# использует для закрытия локатор бокового меню

x = 647  # координата x для возврата из раздела поддержки
y = 363  # координата y для возврата из раздела поддержки


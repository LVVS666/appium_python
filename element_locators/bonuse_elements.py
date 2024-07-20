from appium.webdriver.common.appiumby import AppiumBy

#Кнопки основного функционала
main_menu = (
    AppiumBy.ACCESSIBILITY_ID,
    'Открыть навигацию'
)
bonuse_menu_button = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/menuText" and @text="Бонусы"]'
)

bonuse_count_menu = (
    AppiumBy.ID,
    'ru.berizaryad.android.staging:id/tvCountBonus'
)

enter_promocode_button = (
    AppiumBy.ID,
    'ru.berizaryad.android.staging:id/btnEnterPromoCode'
)

form_promocode = (
    AppiumBy.ID,
    'ru.berizaryad.android.staging:id/inputPromoCode'
)

send_promocode = (
    AppiumBy.ID,
    'ru.berizaryad.android.staging:id/btActivate'
)

bunuse_count = (
    AppiumBy.ID,
    'ru.berizaryad.android.staging:id/tvBonusCount'
)

gift_button = (
    AppiumBy.ID,
    'ru.berizaryad.android.staging:id/btnTakeGift'
)

gift_page = (
    AppiumBy.ID,
    'ru.berizaryad.android.staging:id/webViewGift'
)


#Уведомление о добавление промокода
not_promocode = (
    AppiumBy.XPATH,
    '//android.widget.Toast[@text="Такого промокода нет :("]'
)
success_promocode = (
    AppiumBy.XPATH,
    '//android.widget.Toast[@text="Промокод применен"]'
)

not_activate_promocode = (
    AppiumBy.XPATH,
    '//android.widget.Toast[@text="Этот промокод уже применен. Повторно активировать его не получится"]'
)

new_user_promocode = 'sccn8'
old_user_promocode = 'sccn81'
count_0_promocode = 'sccn811'
expiry_promocode = 'uw6mf'
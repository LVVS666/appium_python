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

button_close = (
    AppiumBy.XPATH,
    '//android.widget.Button[@resource-id="ru.berizaryad.android.staging:id/btnClose"]'
)


'''Документы Российской Федерации'''
russian_consent = (
    AppiumBy.XPATH,
    '(//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvDocumentName"])[1]'
)
russian_consent_text = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvContent"]'
)
assert_russian_consent_text = 'Пользовательское соглашение России\n'
russian_politice = (
    AppiumBy.XPATH,
    '(//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvDocumentName"])[2]'
)
russian_politice_text = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvContent"]'
)
assert_russian_politice_text = 'Персональные данные России\n'
russian_requisites = (
    AppiumBy.XPATH,
    '(//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvDocumentName"])[3]'
)
russian_requisites_text = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvContent"]'
)
assert_russian_requisites_text = 'Реквизиты России\n'


'''Документы Казахстана'''
kazahstan_consent = (
    AppiumBy.XPATH,
    '(//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvDocumentName"])[4]'
)
kazahstan_consent_text = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvContent"]'
)
assert_kazahstan_consent_text = 'Пользовательское соглашение Казахстана \n'
kazahstan_politice = (
    AppiumBy.XPATH,
    '(//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvDocumentName"])[5]'
)
kazahstan_politice_text = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvContent"]'
)
assert_kazahstan_politice_text = 'Персональные данные Казахстана\n'
kazahstan_requisites = (
    AppiumBy.XPATH,
    '(//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvDocumentName"])[6]'
)
kazahstan_requisites_text = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvContent"]'
)
assert_kazahstan_requisites_text = 'Реквизиты Казахстана\n'


'''Документы Киргизстана'''
kirgistan_consent = (
    AppiumBy.XPATH,
    '(//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvDocumentName"])[7]'
)
kirgistan_consent_text = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvContent"]'
)
assert_kirgistan_consent_text = 'Пользовательское соглашение Киргизии\n'
kirgistan_politice = (
    AppiumBy.XPATH,
    '(//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvDocumentName"])[8]'
)
kirgistan_politice_text = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvContent"]'
)
assert_kirgiztan_politice_text = 'Персональные данные Киргизии\n'
kirgistan_requisites = (
    AppiumBy.XPATH,
    '(//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvDocumentName"])[9]'
)
kirgistan_requisites_text = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvContent"]'
)
assert_kirgistan_requisites_text = 'Реквизиты Киргизии\n'


'''Документы Беларуси'''
belarussia_consent = (
    AppiumBy.XPATH,
    '(//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvDocumentName"])[10]'
)
belarussia_consent_text = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvContent"]'
)
assert_belarussia_consent_text = 'Пользовательское соглашение Беларуси\n'
belarussia_politice = (
    AppiumBy.XPATH,
    '(//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvDocumentName"])[11]'
)
belarussia_politice_text = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvContent"]'
)
assert_belarussia_politice_text = 'Персональные данные Беларуси\n'
belarussia_requisites = (
    AppiumBy.XPATH,
    '(//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvDocumentName"])[12]'
)
belarussia_requisites_text = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="ru.berizaryad.android.staging:id/tvContent"]'
)
assert_belarussia_requisites_text = 'Реквизиты Беларуси\n'

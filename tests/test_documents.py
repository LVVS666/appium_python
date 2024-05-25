from page.android_app import AndroidApp


def test_list_country_in_doc(driver_android):
    '''Проверка отображения содержимого раздела документов'''
    app_login = AndroidApp(driver_android)
    app_login.documents()


def test_all_doc_in_russia(driver_android):
    '''Проверка документов у Российской Федерации'''
    app_login = AndroidApp(driver_android)
    app_login.documents_in_russia()


def test_all_doc_in_kazahstan(driver_android):
    '''Проверка документов у Казахстана'''
    app_login = AndroidApp(driver_android)
    app_login.documents_in_kazahstan()


def test_all_doc_in_kirgistan(driver_android):
    '''Проверка документов у Киргизии'''
    app_login = AndroidApp(driver_android)
    app_login.documents_in_kirgistan()

def test_all_doc_in_belarussia(driver_android):
    '''Проверка документов у Беларуси'''
    app_login = AndroidApp(driver_android)
    app_login.documents_in_belarussia()



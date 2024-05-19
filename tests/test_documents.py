from element_locators import doc_elements as doc_el
from page.android_app import AndroidApp


def test_list_country_in_doc(driver_android):
    '''Проверка отображения содержимого раздела документов'''
    app_login = AndroidApp(driver_android)
    app_login.documents()


def test_all_doc_in_russia(driver_android):
    '''Проверка документов у Российской Федерации'''
    app_login = AndroidApp(driver_android)
    app_login.documents_in_country(
        user_consent=doc_el.russian_consent,
        consent_text=doc_el.russian_consent_text,
        assert_consent=doc_el.assert_russian_consent_text,
        politice_date=doc_el.russian_politice,
        politice_text=doc_el.russian_politice_text,
        assert_politice=doc_el.assert_russian_politice_text,
        requisites=doc_el.russian_requisites,
        requisites_text=doc_el.russian_requisites_text,
        assert_requisites=doc_el.assert_russian_requisites_text
    )


def test_all_doc_in_kazahstan(driver_android):
    '''Проверка документов у Казахстана'''
    app_login = AndroidApp(driver_android)
    app_login.documents_in_country(
        user_consent=doc_el.kazahstan_consent,
        consent_text=doc_el.kazahstan_consent_text,
        assert_consent=doc_el.assert_kazahstan_consent_text,
        politice_date=doc_el.kazahstan_politice,
        politice_text=doc_el.kazahstan_politice_text,
        assert_politice=doc_el.assert_kazahstan_politice_text,
        requisites=doc_el.kazahstan_requisites,
        requisites_text=doc_el.kazahstan_requisites_text,
        assert_requisites=doc_el.assert_kazahstan_requisites_text
    )


def test_all_doc_in_kirgistan(driver_android):
    '''Проверка документов у Киргизии'''
    app_login = AndroidApp(driver_android)
    app_login.documents_in_country(
        user_consent=doc_el.kirgistan_consent,
        consent_text=doc_el.kirgistan_consent_text,
        assert_consent=doc_el.assert_kirgistan_consent_text,
        politice_date=doc_el.kirgistan_politice,
        politice_text=doc_el.kirgistan_politice_text,
        assert_politice=doc_el.assert_kirgiztan_politice_text,
        requisites=doc_el.kirgistan_requisites,
        requisites_text=doc_el.kirgistan_requisites_text,
        assert_requisites=doc_el.assert_kirgistan_requisites_text
    )

def test_all_doc_in_belarussia(driver_android):
    '''Проверка документов у Беларуси'''
    app_login = AndroidApp(driver_android)
    app_login.documents_in_country(
        user_consent=doc_el.belarussia_consent,
        consent_text=doc_el.belarussia_consent_text,
        assert_consent=doc_el.assert_belarussia_consent_text,
        politice_date=doc_el.belarussia_politice,
        politice_text=doc_el.belarussia_politice_text,
        assert_politice=doc_el.assert_belarussia_politice_text,
        requisites=doc_el.belarussia_requisites,
        requisites_text=doc_el.belarussia_requisites_text,
        assert_requisites=doc_el.assert_belarussia_requisites_text
    )



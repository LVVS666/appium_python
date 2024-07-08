from element_locators import auth_elements as el_auth
from element_locators import doc_elements as el_doc
from page.base_app import BaseApp


class Documents(BaseApp):
    '''Класс Документов для всех стран'''
    def documents(self):
        '''Проверка наличия всех стран в документах'''
        self.click_element(el_auth.outside_map)
        self.click_element(el_auth.main_menu)
        self.click_element(el_doc.documents)
        self.wait(el_doc.russian_documents)
        assert self.find(el_doc.russian_documents),'В документах отсутствует раздел Российской Федерации'
        assert self.find(el_doc.kazahstan_documents), 'В документах отсутствует раздел Казахстана'
        assert self.find(el_doc.kirgistan_documents), 'В документах отсутствует раздел Кыргызстан'
        assert self.find(el_doc.belarussia_documents), 'В документах отсутствует раздел Беларуссии'
        self.click_element(el_doc.button_back_documents)

    def documents_in_country(
                             self,
                             user_consent,
                             consent_text,
                             assert_consent,
                             politice_date,
                             politice_text,
                             assert_politice,
                             requisites,
                             requisites_text,
                             assert_requisites
                            ):
        '''Проверка документов у стран'''
        self.click_element(el_auth.outside_map)
        self.click_element(el_auth.main_menu)
        self.click_element(el_doc.documents)
        self.click_element(user_consent)
        self.wait(consent_text)
        assert_consent_text = self.find(consent_text).text
        assert assert_consent_text == assert_consent, 'Текст из <Пользовательского соглашения> не соответствует'
        self.click_element(el_doc.button_close)
        self.click_element(el_auth.outside_map)
        self.click_element(el_auth.main_menu)
        self.click_element(el_doc.documents)
        self.click_element(politice_date)
        self.wait(politice_text)
        assert_politice_text = self.find(politice_text).text
        assert assert_politice_text == assert_politice, 'Текст из <Политика персональных данных> не соответствует'
        self.click_element(el_doc.button_close)
        self.click_element(el_auth.outside_map)
        self.click_element(el_auth.main_menu)
        self.click_element(el_doc.documents)
        self.click_element(requisites)
        self.wait(requisites_text)
        assert_requisites_text = self.find(requisites_text).text
        assert assert_requisites_text == assert_requisites, 'Текст из <Реквизиты> не соответствует'
        self.click_element(el_doc.button_close)
        self.wait(el_auth.outside_map)

    def documents_in_russia(self):
        '''Проверка документов у России'''
        self.documents_in_country(
            user_consent=el_doc.russian_consent,
            consent_text=el_doc.russian_consent_text,
            assert_consent=el_doc.assert_russian_consent_text,
            politice_date=el_doc.russian_politice,
            politice_text=el_doc.russian_politice_text,
            assert_politice=el_doc.assert_russian_politice_text,
            requisites=el_doc.russian_requisites,
            requisites_text=el_doc.russian_requisites_text,
            assert_requisites=el_doc.assert_russian_requisites_text
        )

    def documents_in_kazahstan(self):
        '''Проверка документов у Казахстана'''
        self.documents_in_country(
            user_consent=el_doc.kazahstan_consent,
            consent_text=el_doc.kazahstan_consent_text,
            assert_consent=el_doc.assert_kazahstan_consent_text,
            politice_date=el_doc.kazahstan_politice,
            politice_text=el_doc.kazahstan_politice_text,
            assert_politice=el_doc.assert_kazahstan_politice_text,
            requisites=el_doc.kazahstan_requisites,
            requisites_text=el_doc.kazahstan_requisites_text,
            assert_requisites=el_doc.assert_kazahstan_requisites_text
        )

    def documents_in_kirgistan(self):
        '''Проверка документов у Киргизтана'''
        self.documents_in_country(
            user_consent=el_doc.kirgistan_consent,
            consent_text=el_doc.kirgistan_consent_text,
            assert_consent=el_doc.assert_kirgistan_consent_text,
            politice_date=el_doc.kirgistan_politice,
            politice_text=el_doc.kirgistan_politice_text,
            assert_politice=el_doc.assert_kirgiztan_politice_text,
            requisites=el_doc.kirgistan_requisites,
            requisites_text=el_doc.kirgistan_requisites_text,
            assert_requisites=el_doc.assert_kirgistan_requisites_text
        )

    def documents_in_belarussia(self):
        '''Проверка документов у Беларуси'''
        self.documents_in_country(
            user_consent=el_doc.belarussia_consent,
            consent_text=el_doc.belarussia_consent_text,
            assert_consent=el_doc.assert_belarussia_consent_text,
            politice_date=el_doc.belarussia_politice,
            politice_text=el_doc.belarussia_politice_text,
            assert_politice=el_doc.assert_belarussia_politice_text,
            requisites=el_doc.belarussia_requisites,
            requisites_text=el_doc.belarussia_requisites_text,
            assert_requisites=el_doc.assert_belarussia_requisites_text
        )
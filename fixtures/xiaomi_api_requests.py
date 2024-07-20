import hashlib
import hmac
import json
import requests


class XiaomiApi:
    base_url = 'https://stagemobileapi.berizaryad.ru/auth/api/v2'
    signature_key = None #Добавить env файл с приватным ключом
    xiaomi_payload = {
        "app_version": "5.5.0",
        "os_version": "34",
        "platform": "Android",
        "udid": "9431f444e5844793"
    }

    def generate_signature(self, raw_data):
        '''Генерация сигнатуры'''
        msg = json.dumps(raw_data).encode()
        messenger_key = self.signature_key.encode()
        signature = hmac.new(messenger_key, msg, digestmod=hashlib.sha256).hexdigest()
        return {'Locale': 'ru', 'signature': signature, 'Content-Type': 'application/json'}

    def xiaomi_api_login(self, number):
        '''Запрос на логин'''
        url = "/login"
        data_json = self.xiaomi_payload
        data_json['phone'] = number
        return requests.post(url=self.base_url+url, json=data_json, headers=self.generate_signature(data_json))

    def xiaomi_api_confirm(self, number):
        '''Запрос на ввод смс кода'''
        url = "/confirm"
        data_json = self.xiaomi_payload
        data_json['phone'] = number
        data_json['code'] = "0001"
        return requests.post(url=self.base_url+url, json=data_json, headers=self.generate_signature(data_json))

    def xiaomi_api_users(self, token):
        '''Запрос на получение информации о пользователе'''
        url = "/users"
        headers = {
            'Authorization': f'Bearer {token}'
        }
        return requests.get(url=self.base_url+url, headers=headers)


kl = XiaomiApi()
kl.xiaomi_api_login("79992769943")
token = kl.xiaomi_api_confirm("79992769943").json()
print(kl.xiaomi_api_users(token['access_token']))

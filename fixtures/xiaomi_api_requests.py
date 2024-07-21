import hashlib
import hmac
import json
import requests
import os

from dotenv import load_dotenv

load_dotenv()


class XiaomiApi:
    base_url = 'https://stageapi.berizaryad.ru'
    signature_key = os.getenv('signature_key')
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
        url = "/auth/api/v2/login"
        data_json = self.xiaomi_payload
        data_json['phone'] = number
        return requests.post(url=self.base_url+url, json=data_json, headers=self.generate_signature(data_json))

    def xiaomi_api_confirm(self, number):
        '''Запрос на ввод смс кода'''
        url = "/auth/api/v2/confirm"
        data_json = self.xiaomi_payload
        data_json['phone'] = number
        data_json['code'] = "0001"
        return requests.post(url=self.base_url+url, json=data_json, headers=self.generate_signature(data_json))

    def xiaomi_api_users(self, token):
        '''Запрос на получение информации о пользователе'''
        url = "/users"
        headers = {
            "authorization": f"Bearer {token}"
        }
        return requests.get(url=self.base_url+url, headers=headers)

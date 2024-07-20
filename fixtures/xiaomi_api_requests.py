import requests


class XiaomiApi:
    base_url = 'https://stageapi.berizaryad.ru/auth/api/v2'
    signature = 'b535be8d7d730c4d2c43bb822c49417cfce43a357aae759d62271f0811049ad0'
    headers = {
        'Content-Type': 'application/json',
        'signature': signature
    }

    def xiaomi_api_login(self, number):
        url = "/login"
        xiaomi_login_payload = {
            "app_version": "5.5.0",
            "os_version": "34",
            "phone": number,
            "platform": "Android",
            "udid": "9431f444e5844793"
        }
        return requests.post(url=self.base_url+url, params=xiaomi_login_payload, headers=self.headers)


    def xiaomi_api_confirm(self, number):
        url = "/confirm"
        xiaomi_confirm_payload = {
            "app_version": "5.5.0",
            "code": "0001",
            "os_version": "34",
            "phone": number,
            "platform": "Android",
            "udid": "9431f444e5844793"
        }
        response_data = requests.post(url=self.base_url+url, params=xiaomi_confirm_payload, headers=self.headers)
        return response_data.json()


kl = XiaomiApi()
kl.xiaomi_api_login("79992769943")
print(kl.xiaomi_api_confirm("79992769943"))
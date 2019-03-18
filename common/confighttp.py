import requests
from common.readconfig import ReadConfig
from common.get_token import get_token

token = get_token()


class ConfigHttp:
    def __init__(self):
        global url, timeout
        config = ReadConfig()
        url = config.get_config_value('apiDomain','domain')
        timeout = config.get_config_value('apiDomain','timeout')
        self.data = {}
        self.headers = {}
        self.url = None
        self.files = {}

    def set_url(self, para_api):   #拼接ip方法
        self.url = url+para_api
        return self.url

    def set_url2(self, para_api):
        self.url = para_api
        return self.url

    def set_headers(self, headers={}):
        self.headers['Authorization'] = token
        self.headers['Content-Type'] = 'application/json;charset=UTF-8'
        self.headers['appKey'] = '2d99a4c9-93f2-4b51-a058-beebd4a5cba7'
        self.headers['secret'] = '6de11e5e-48f3-4bd5-9b02-1fbc9f56da19'
        self.headers['X-APP-INFO'] = '{"channel":"APP-GW1-Android-1.0.9","deviceType":"android","imei":"99001087507262","mac":"Failed","manufacturer":"Xiaomi","model":"MIMAX 2","os":"7.1.1","version":"1.0.9"}'
        return self.headers

    def set_data(self, data):
        self.data = data

    def set_files(self,file):
        self.files = file

    def get(self):
        try:
            response = requests.get(self.url, headers=self.headers, params=self.data, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error('TIME OUT %s .'%self.url)

    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, json=self.data, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error('TIME OUT %s .'%self.url)




if __name__ == '__main__':
    a = ConfigHttp()
    hearder = "{}"
    hearders = a.set_headers(hearder)
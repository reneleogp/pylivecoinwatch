import requests
import json

from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.util.retry import Retry

# from .utils import func_args_preprocessing


class LiveCoinWatchAPI:
    base_url = 'https://api.livecoinwatch.com'
    api_key = '8acf6a03-a29b-4cdd-b08c-58bf2ed72678'

    def __init__(self):
        self.api_base_url = LiveCoinWatchAPI.base_url
        self.request_timeout = 120
        self.session = requests.Session()
        self.session.mount('http://', HTTPAdapter(max_retries=5))
        self.headers = {
            'content-type': 'application/json',
            'x-api-key': LiveCoinWatchAPI.api_key
        }

    def set_api(self, user_api_key):
        self.headers['x-api-key'] = user_api_key

    def __request(self, url, payload):
        url = self.api_base_url + url
        response = self.session.post(
            url, headers=self.headers, data=json.dumps(payload))
        return (response.json())

    def status(self):
        url = '/status'
        payload = {}
        return self.__request(url, payload)

    def credits(self):
        url = '/credits'
        payload = {}
        return self.__request(url, payload)

    def overview(self, currency):
        url = '/overview'
        payload = {'currency': currency}
        return self.__request(url, payload)

    def overview_history(self, **kwargs):
        url = '/overview/history'
        payload = {}
        for key, value in kwargs.items():
            payload[key] = value

        return self.__request(url, payload)

    def coin_single(self, **kwargs):
        url = 'coin/single'
        payload = {}
        for key, value in kwargs.items():
            payload[key] = value

        return self.__request(url, payload)


lcw = LiveCoinWatchAPI()

print(lcw.overview_history(currency='BTC', start=1606232700000, end=1606233000000))

from os import error
import requests
import json
import warnings

from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.util.retry import Retry

# from .utils import func_args_preprocessing
SANDBOX_API_KEY = "NO_API"

class LiveCoinWatchAPI:
    base_url = 'https://api.livecoinwatch.com'
    

    def __init__(self, api_key=None):
        self.api_base_url = LiveCoinWatchAPI.base_url
        self.request_timeout = 120
        self.headers = {
            'content-type': 'application/json',
            'x-api-key': SANDBOX_API_KEY if api_key == None else api_key
        }
        self.session = requests.Session()
        self.session.mount('http://', HTTPAdapter(max_retries=5))
        self.session.headers.update(self.headers)

    def set_api_key(self, user_api_key):
        self.headers['x-api-key'] = user_api_key
        self.session.headers.update(self.headers)

    def __request(self, url, payload):
        url = "{}/{}".format(self.api_base_url, url)
        try:
            response = self.session.post(url, data=json.dumps(payload),timeout=self.request_timeout)
        except requests.exceptions.RequestException:
            raise

        try:
            response.raise_for_status()
            content = json.loads(response.content.decode('utf-8'))
            return response
        except Exception as e:
            # check if json (with error message) is returned
            try:
                content = json.loads(response.content.decode('utf-8'))
                raise ValueError(content)
            # if no json
            except json.decoder.JSONDecodeError:
                pass

            raise

    def status(self):
        url = 'status'
        payload = {}
        return self.__request(url, payload)

    def credits(self):
        url = 'credits'
        payload = {}
        return self.__request(url, payload)

    def overview(self, **kwargs):
        url = 'overview'
        return self.__request(url, kwargs)

    def overview_history(self, **kwargs):
        url = 'overview/history'
        return self.__request(url, kwargs)

    def coin_single(self, **kwargs):
        url = 'coins/single'
        return self.__request(url, kwargs)

    def coin_single_history(self, **kwargs):
        url = 'coins/single/history'
        return self.__request(url, kwargs)

    def coin_list(self, **kwargs):
        url = "coins/list"
        return self.__request(url, kwargs)

    def fiats_all(self):
        url = "fiats/all"
        payload = {}
        return self.__request(url, payload)

    def exchanges_single(self, **kwargs):
        url = 'exchanges/single'
        return self.__request(url, kwargs)

    def exchanges_list(self, **kwargs):
        url = 'exchanges/list'
        return self.__request(url, kwargs)


lcw = LiveCoinWatchAPI()

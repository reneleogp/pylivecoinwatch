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
            response = self.session.post(url, data=json.dumps(
                payload), timeout=self.request_timeout)
        except requests.exceptions.RequestException:
            raise

        try:
            # if(response.status_code == 500 and self.__request('status', {}).status_code == 200):
            response.raise_for_status()
            content = json.loads(response.content.decode('utf-8'))
            return content
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
        payload = kwargs
        return self.__request(url, payload)

    def overview_history(self, start, end, **kwargs):
        url = 'overview/history'
        payload = kwargs
        payload['start'] = start
        payload['end'] = end
        return self.__request(url, payload)

    def coins_single(self, code, **kwargs):
        url = 'coins/single'
        payload = kwargs
        payload['code'] = code
        return self.__request(url, payload)

    def coins_single_history(self, code, start, end, **kwargs):
        url = 'coins/single/history'
        payload = kwargs
        payload['code'] = code
        payload['start'] = start
        payload['end'] = end
        return self.__request(url, payload)

    def coins_list(self, **kwargs):
        url = "coins/list"
        payload = kwargs
        return self.__request(url, payload)

    def fiats_all(self):
        url = "fiats/all"
        payload = {}
        return self.__request(url, payload)

    def exchanges_single(self, code, **kwargs):
        url = 'exchanges/single'
        payload = kwargs
        payload['code'] = code
        return self.__request(url, payload)

    def exchanges_list(self, **kwargs):
        url = 'exchanges/list'
        payload = kwargs
        return self.__request(url, payload)

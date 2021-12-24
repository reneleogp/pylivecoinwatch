import pytest
import unittest
import json

import pylivecoinwatch as api
# from requests.exceptions import HTTPError

# Enter a valid api key to test
api_key = "8acf6a03-a29b-4cdd-b08c-58bf2ed72678"

lcw = api.LiveCoinWatchAPI(api_key)
lcw_without_key = api.LiveCoinWatchAPI()


class TestWrapper(unittest.TestCase):

    def test_bad_init(self):
        with pytest.raises(ValueError):
            response = lcw_without_key.overview(currency="USD")
            
    def test_set_api_key(self):
        lcw_without_key.set_api_key(api_key)
        response = lcw_without_key.overview(currency="USD")
        self.assertEqual(response.status_code, 200)

    def test_status(self):
        response = lcw.status()
        self.assertEqual(response.status_code, 200)

    def test_credits(self):
        response = lcw.credits()
        self.assertEqual(response.status_code, 200)

    def test_overview(self):
        response = lcw.overview(currency="USD")
        self.assertEqual(response.status_code, 200)

    def test_overview_history(self):
        response = lcw.overview_history(
            currency="USD", start=1606232700000, end=1606233000000)
        self.assertEqual(response.status_code, 200)

    def test_coins_single(self):
        response = lcw.coin_single(currency='USD', code='ETH', meta=True)
        self.assertEqual(response.status_code, 200)

        response = lcw.coin_single(currency='USD', code='ETH', meta=False)
        self.assertEqual(response.status_code, 200)

    def test_coins_single_history(self):
        response = lcw.coin_single_history(
            currency='USD', code='BTC', meta=True, start=1606232700000, end=1606233000000)
        self.assertEqual(response.status_code, 200)

        response = lcw.coin_single_history(
            currency='USD', code='BTC', meta=False, start=1606232700000, end=1606233000000)
        self.assertEqual(response.status_code, 200)

    def test_coins_list(self):
        response = lcw.coin_list(
            currency="USD", sort="rank", order="ascending", meta=True)
        self.assertEqual(response.status_code, 200)

        response = lcw.coin_list(
            currency="USD", sort="rank", order="ascending", meta=False)
        self.assertEqual(response.status_code, 200)

    def test_fiats_all(self):
        response = lcw.fiats_all()
        self.assertEqual(response.status_code, 200)

    def test_exchanges_single(self):
        response = lcw.exchanges_single(
            currency="ETH", code='gemini', meta=True)
        self.assertEqual(response.status_code, 200)

        response = lcw.exchanges_single(
            currency="ETH", code='gemini', meta=False)
        self.assertEqual(response.status_code, 200)

    def test_exchanges_list(self):
        response = lcw.exchanges_list(
            currency="USD", sort="visitors", order="descending", meta=True)
        self.assertEqual(response.status_code, 200)

        response = lcw.exchanges_list(
            currency="USD", sort="visitors", order="descending", meta=False)
        self.assertEqual(response.status_code, 200)

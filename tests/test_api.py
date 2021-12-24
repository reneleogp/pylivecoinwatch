import pytest
import unittest
import json

from pylivecoinwatch import LiveCoinWatchAPI
# from requests.exceptions import HTTPError

# Enter a valid api key to test
api_key = "8acf6a03-a29b-4cdd-b08c-58bf2ed72678"


class TestWrapper(unittest.TestCase):

    def setUp(self):
        self.lcw = LiveCoinWatchAPI(api_key)
        self.lcw_without_key = LiveCoinWatchAPI()

    def test_bad_init(self):
        with pytest.raises(ValueError):
            response = self.lcw_without_key.overview(currency="USD")

    def test_set_api_key(self):
        self.lcw_without_key.set_api_key(api_key)
        response = self.lcw_without_key.overview(currency="USD")
        self.assertEqual(response.status_code, 200)

    def test_status(self):
        response = self.lcw.status()
        self.assertEqual(response.status_code, 200)

    def test_credits(self):
        response = self.lcw.credits()
        self.assertEqual(response.status_code, 200)

    def test_overview(self):
        response = self.lcw.overview(currency="USD")
        self.assertEqual(response.status_code, 200)

    def test_overview_history(self):
        response = self.lcw.overview_history(
            currency="USD", start=1606232700000, end=1606233000000)
        self.assertEqual(response.status_code, 200)

    def test_coins_single(self):
        response = self.lcw.coin_single(currency='USD', code='ETH', meta=True)
        self.assertEqual(response.status_code, 200)

        response = self.lcw.coin_single(currency='USD', code='ETH', meta=False)
        self.assertEqual(response.status_code, 200)

    def test_coins_single_history(self):
        response = self.lcw.coin_single_history(
            currency='USD', code='BTC', meta=True, start=1606232700000, end=1606233000000)
        self.assertEqual(response.status_code, 200)

        response = self.lcw.coin_single_history(
            currency='USD', code='BTC', meta=False, start=1606232700000, end=1606233000000)
        self.assertEqual(response.status_code, 200)

    def test_coins_list(self):
        response = self.lcw.coin_list(
            currency="USD", sort="rank", order="ascending", meta=True)
        self.assertEqual(response.status_code, 200)

        response = self.lcw.coin_list(
            currency="USD", sort="rank", order="ascending", meta=False)
        self.assertEqual(response.status_code, 200)

    def test_fiats_all(self):
        response = self.lcw.fiats_all()
        self.assertEqual(response.status_code, 200)

    def test_exchanges_single(self):
        response = self.lcw.exchanges_single(
            currency="ETH", code='gemini', meta=True)
        self.assertEqual(response.status_code, 200)

        response = self.lcw.exchanges_single(
            currency="ETH", code='gemini', meta=False)
        self.assertEqual(response.status_code, 200)

    def test_exchanges_list(self):
        response = self.lcw.exchanges_list(
            currency="USD", sort="visitors", order="descending", meta=True)
        self.assertEqual(response.status_code, 200)

        response = self.lcw.exchanges_list(
            currency="USD", sort="visitors", order="descending", meta=False)
        self.assertEqual(response.status_code, 200)

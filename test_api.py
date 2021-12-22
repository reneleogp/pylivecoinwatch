import pytest
import requests
import responses
import unittest
import unittest.mock as mock
import json

import pylivecoinwatch as api
from requests.exceptions import HTTPError

lcw = api.LiveCoinWatchAPI()


class TestWrapper(unittest.TestCase):

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

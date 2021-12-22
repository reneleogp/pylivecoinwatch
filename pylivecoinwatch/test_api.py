import pytest
import requests
import responses
import unittest
import unittest.mock as mock
import json

from .api import LiveCoinWatchAPI
from requests.exceptions import HTTPError

lcw = LiveCoinWatchAPI()


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
        response = lcw.coin_single()
        self.assertEqual(response.status_code, 200)

    def test_coins_single_history(self):
        response = lcw.coin_single_history()
        self.assertEqual(response.status_code, 200)

    def test_coins_list(self):
        response = lcw.coin_list()
        self.assertEqual(response.status_code, 200)

    def test_fiats_all(self):
        response = lcw.fiats_all()
        self.assertEqual(response.status_code, 200)

    def test_exchanges_single(self):
        response = lcw.exchanges_single()
        self.assertEqual(response.status_code, 200)

    def test_exchanges_list(self):
        response = lcw.exchanges_list()
        self.assertEqual(response.status_code, 200)

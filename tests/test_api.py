import pytest
import unittest
import json
import os

from pylivecoinwatch import LiveCoinWatchAPI

# from requests.exceptions import HTTPError

# Enter a valid api key to test
api_key = os.environ["LCW_API_KEY"]
# api_key = "YOUR_API_KEY"


class TestWrapper(unittest.TestCase):
    def setUp(self):
        self.lcw = LiveCoinWatchAPI(api_key)
        self.lcw_without_key = LiveCoinWatchAPI()

    def test_bad_init(self):
        with pytest.raises(ValueError):
            response = self.lcw_without_key.overview(currency="USD")

    def test_set_api_key(self):
        self.lcw_without_key.set_api_key(api_key)
        response = self.lcw_without_key.credits()
        expected = {"dailyCreditsRemaining", "dailyCreditsLimit"}
        for item in expected:
            self.assertIn(item, response)

    def test_status(self):
        response = self.lcw.status()
        self.assertEqual(response, {})

    def test_credits(self):
        expected = {"dailyCreditsRemaining", "dailyCreditsLimit"}
        response = self.lcw.credits()
        for item in expected:
            self.assertIn(item, response)

    def test_overview(self):
        expected = {"cap", "volume", "liquidity", "btcDominance"}
        response = self.lcw.overview(currency="USD")
        for item in expected:
            self.assertIn(item, response)

    def test_overview_history(self):
        expected_response = [
            {
                "date": 1606232700000,
                "cap": 581171117946,
                "volume": 56158051529,
                "liquidity": 1295845494,
                "btcDominance": 0.6144324552690166,
            },
            {
                "date": 1606233000000,
                "cap": 582049608242,
                "volume": 56643100921,
                "liquidity": 1265635689,
                "btcDominance": 0.6128301980588141,
            },
        ]
        response = self.lcw.overview_history(
            currency="USD", start=1606232700000, end=1606233000000
        )
        self.assertEqual(response, expected_response)

    def test_coins_single(self):
        expected = {"cap", "volume", "cap"}
        response = self.lcw.coins_single(currency="USD", code="ETH", meta=False)
        for item in expected:
            self.assertIn(item, response)

    def test_coins_single_history(self):
        expected_response = {
            "history": [
                {
                    "date": 1666644900000,
                    "rate": 19386.515935092288,
                    "volume": 16515810007,
                    "cap": 371995369362,
                    "liquidity": 1118559501,
                },
                {
                    "date": 1666645200000,
                    "rate": 19388.58794695064,
                    "volume": 16501101547,
                    "cap": 372035127863,
                    "liquidity": 1165993966,
                },
            ]
        }
        response = self.lcw.coins_single_history(
            currency="USD",
            code="BTC",
            meta=False,
            start=1666644877019,
            end=1666645200000,
        )
        self.assertEqual(response, expected_response)

    def test_coins_list(self):
        expected = {"code", "rate", "cap", "volume"}
        response = self.lcw.coins_list(
            currency="USD", sort="rank", order="ascending", meta=False
        )
        for item in expected:
            for item2 in response:
                self.assertIn(item, item2)

    def test_fiats_all(self):
        expected = {"code", "countries", "name", "flag"}
        response = self.lcw.fiats_all()
        for item in expected:
            for item2 in response:
                self.assertIn(item, item2)

    def test_exchanges_single(self):
        expected = {
            "code",
            "markets",
            "bidTotal",
            "volume",
            "askTotal",
            "depth",
            "visitors",
            "volumePerVisitor",
        }
        response = self.lcw.exchanges_single(currency="ETH", code="gemini", meta=False)
        for item in expected:
            self.assertIn(item, response)

    def test_exchanges_list(self):
        expected = {
            "code",
            "markets",
            "bidTotal",
            "askTotal",
            "visitors",
            "volumePerVisitor",
        }
        response = self.lcw.exchanges_list(
            currency="USD", sort="visitors", order="descending", meta=False
        )
        for item in expected:
            for item2 in response:
                self.assertIn(item, item2)

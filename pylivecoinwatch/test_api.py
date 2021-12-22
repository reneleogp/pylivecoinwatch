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
        print(response.status_code)

    def test_credits(self):
        response = lcw.credits()

        self.assertEqual(response.status_code, 200)

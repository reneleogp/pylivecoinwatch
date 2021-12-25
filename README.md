# LiveCoinWatch API wrapper

Python3 wrapper around the [LiveCoinWatch](https://www.livecoinwatch.com/) API

[![PyPi Version](https://img.shields.io/pypi/v/pylivecoinwatch.svg)](https://pypi.python.org/pypi/pylivecoinwatch/)
![GitHub](https://img.shields.io/github/license/PlayErphil/LCW-API-Wrapper)

## Installation
PyPI
```bash
pip install pylivecoinwatch
```
or from source
```bash
git clone https://github.com/PlayErphil/pylivecoinwatch.git
cd pylivecoinwatch
python3 setup.py install
```

## Usage

Create the class.

```python
from pylivecoinwatch import LiveCoinWatchAPI
lcw = LiveCoinWatchAPI("<YOUR_API_KEY>")
```

**The package has no API key, so make sure to get one from the [API playground](https://www.livecoinwatch.com/tools/api) and pass it as a parameter when creating the class.**

## API Key Error
If your API key is wrong or you didn't specify one, the class will raise 401 Error.

401 Error example:
```python
>>> from pylivecoinwatch import LiveCoinWatchAPI
>>> lcw = LiveCoinWatchAPI()
>>> lcw.overview()

Traceback (most recent call last):

raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://api.livecoinwatch.com/overview

During handling of the above exception, another exception occurred:

Traceback (most recent call last):

ValueError: {'error': {'code': 401, 'status': 'Unauthorized', 'description': 'The requester is not authorized to access the resource. This is similar to 403 but is used in cases where authentication is expected but has failed or has not been provided.'}}

```

If you wished to change your API key at any point you can use the following function:
```python
lcw.set_api_key("<NEW_API_KEY>")
# This will change your API key to <NEW_API_KEY>
```

## Usage

The required parameters for each endpoint are defined as required (mandatory) parameters for the corresponding functions.
Any optional parameters can be passed using same names, as defined in [LiveCoinWatch API Documentation](https://livecoinwatch.github.io/lcw-api-docs/)

**Note that it returns a response object from the request library

Usage examples:
```python
>>> lcw.status
```


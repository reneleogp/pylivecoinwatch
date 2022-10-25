# LiveCoinWatch API wrapper

Python3 wrapper around the [LiveCoinWatch](https://www.livecoinwatch.com/) API

[![PyPi Version](https://img.shields.io/pypi/v/pylivecoinwatch.svg)](https://pypi.python.org/pypi/pylivecoinwatch/)
[![Downloads](https://pepy.tech/badge/pylivecoinwatch)](https://pepy.tech/project/pylivecoinwatch)
![GitHub](https://img.shields.io/github/license/PlayErphil/pylivecoinwatch.svg)

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

_Booleans are supported as input for boolean type parameters; they can be str ('true', 'false') or bool (True, False)
(e.g. see /coins/single usage examples)._

Usage examples:

```python
# /coins/single endpoint without the required parameters
>>> lcw.coins_single()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: coin_single() missing 1 required positional argument: 'code'


# same endpoint with the required parameters
>>> lcw.coins_single(code="BTC")
{'rate': 49810.12848625034, 'volume': 18780569901, 'cap': 942054277908}


# optional parameters can be passed as defined in the API doc (https://livecoinwatch.github.io/lcw-api-docs/)
>>> lcw.coins_single(currency="EUR", code="BTC", meta='true')
# OR (also booleans can be used for boolean type arguments)
>>> lcw.coin_single(currency="EUR", code="BTC", meta=True)
# both return the same thing
{'name': 'Bitcoin', 'symbol': '₿', 'color': '#fa9e32', 'png32': 'https://lcw.nyc3.cdn.digitaloceanspaces.com/production/currencies/32/btc.png', 'png64': 'https://lcw.nyc3.cdn.digitaloceanspaces.com/production/currencies/64/btc.png', 'webp32': 'https://lcw.nyc3.cdn.digitaloceanspaces.com/production/currencies/32/btc.webp', 'webp64': 'https://lcw.nyc3.cdn.digitaloceanspaces.com/production/currencies/64/btc.webp', 'exchanges': 171, 'markets': 4483, 'pairs': 1604, 'allTimeHighUSD': 68780.77475755227, 'circulatingSupply': 18912906, 'totalSupply': 18912906, 'maxSupply': 21000000, 'rate': 43399.258910010154, 'volume': 17172466006, 'cap': 820806104234}
```

## API Documentation

https://livecoinwatch.github.io/lcw-api-docs/

## Enpoints included

> :warning: **Endpoints documentation**: To make sure that your are using properly each endpoint you should check the [API documentation](https://livecoinwatch.github.io/lcw-api-docs/). Return behaviour and parameters of the endpoints, such as _pagination_, might have changed. <br> Any **optional parameters** defined in LiveCoinWatch API doc can be passed as function parameters using same parameters names with the API _(see Examples above)_.

- _status_

  - **/status** (Check API server status)
    ```python
    lcw.status()
    ```
    Example:
    ```python
    >>> lcw.status()
    {}
    ```

- _credits_

  - **/credits** (Get your API key related information.)
    ```python
    lcw.credits()
    ```
    Example:
    ```python
    >>> lcw.credits()
    {'dailyCreditsRemaining': 9995, 'dailyCreditsLimit': 10000}
    ```

- _overview_

  - **/overview** (Get current aggregated data for all coins.)

    ```python
    lcw.overview()
    ```

    Example:

    ```python
    >>> lcw.overview()
    {'cap': 2401907143522, 'volume': 70680847315, 'liquidity': 5779984192, 'btcDominance': 0.3927240083177512}
    ```

  - **/overview/history** (Get historical aggregated data of entire market.)
    ```python
    lcw.overview_history()
    ```
    Example:
    ```python
    >>> lcw.overview_history(start="1606232700000", end="1606232700000")
    [{'date': 1606232700000, 'cap': 581171117946, 'volume': 56158051529, 'liquidity': 1295845494, 'btcDominance': 0.6144324552690166}]
    ```

- _coins_

  - **/coins/single** (Get all information about a single coin at latest moment in time.)

    ```python
    lcw.coins_single()
    ```

    Example:

    ```python
    >>> lcw.coins_single(code="BTC")
    {'rate': 49810.12848625034, 'volume': 18780569901, 'cap': 942054277908}
    ```

  - **/coins/single/history** (Get historical information about a single coin.)

    ```python
    lcw.coins_single_history()
    ```

    Example:

    ```python
    >>> lcw.coins_single_history(start=1617035100000, end=1617035400000, code="ETH")
    {'history': [{'date': 1617035100000, 'rate': 1783.635049099136, 'volume': 7615440037, 'cap': 205564989970}, {'date': 1617035400000, 'rate': 1785.1535622292442, 'volume': 7682072359, 'cap': 205741029536}]}
    ```

  - **/coins/list** (Get assorted information for a list of coins.)
    ```python
    lcw.coins_list()
    ```
    Example:
    ```python
    >>> lcw.coins_list(limit=2, sort="rank", order="ascending")
    [{'code': 'BTC', 'rate': 49741.45295774467, 'volume': 18786805838, 'cap': 940755424093}, {'code': 'ETH', 'rate': 3944.8091570473284, 'volume': 10458770693, 'cap': 469117284843}]
    ```

- _fiats_

  - **/fiats/all** (Get list of all the fiats.)
    ```python
    lcw.fiats_all()
    ```
    Example:
    ```python
    >>> lcw.fiats_all()
    [{'code': 'PAB', 'countries': ['PAN'], 'flag': 'PAN', 'name': 'Panamanian Balboa', 'symbol': 'B/.'}, {'code': 'AZN', 'countries': ['AZE'], 'flag': 'AZE', 'name': 'Azerbaijani Manat', 'symbol': '₼'}    ...............    {'code': 'PKR', 'countries': ['PAK'], 'flag': 'PAK', 'name': 'Pakistani Rupee', 'symbol': '₨'}]
    ```

- _exchanges_

  - **/exchanges/single** (Get assorted exchange information.)

    ```python
    lcw.exchanges_single()
    ```

    Example:

    ```python
    >>> lcw.exchanges_single(code="kucoin")
    {'code': 'kucoin', 'markets': 947, 'volume': 2916293370, 'bidTotal': 40050156.01994438, 'askTotal': 45237792.80490364, 'depth': 85287948.82484803, 'visitors': 94003, 'volumePerVisitor': 31023.407444443263}
    ```

  - **/exchanges/list** (Get assorted information on list of exchanges.)
    ```python
    lcw.exchanges_list()
    ```
    Example:
    ```python
    >>> lcw.exchanges_list(sort="visitors", order="descending", limit=2, offset=1)
    [{'code': 'binance', 'markets': 1302, 'volume': 16969814270, 'bidTotal': 360409773.5276142, 'askTotal': 307530423.509523, 'depth': 667940197.0371372, 'visitors': 1303774, 'volumePerVisitor': 13015.91707611902}, {'code': 'pancakeswapv2', 'markets': 3416, 'volume': 337585574, 'bidTotal': None, 'askTotal': None, 'depth': 0, 'visitors': 501047, 'volumePerVisitor': 673.7602939444803}]
    ```

## Test

Run unit tests with:

```
# after installing pytest using pip3
pytest tests
Make sure you add an API key for tests.
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

Python script to transfer funds from the Binance futures wallet into spot and accumulate coins running strategies.

<br/>

# **Table of contents**

<!--ts-->
* [Installation](#installation)
    * [Requirements](#requirements)
    * [API Key & Secret](#api-key-&-secret)
    * [Virtual Environment](#virtual-environment)
    * [Install Dependencies](#install-dependencies)
* [General Config](#general-config)
* [Strategies](#strategies)

<br/>

**Installation**
================

Requirements
------------
Base requirements: [Python 3](https://www.python.org/) & [pip](https://pip.pypa.io/en/stable/).

Dependencies are handled using [Pipenv](https://pypi.org/project/pipenv/). To install it:

```sh
$ pip install pipenv
```

<br/>

API Key & Secret
------------
Duplicate the `.env.example` file and rename it to `.env`. Place your Binance API key and secret in there.


<br/>

Virtual Environment
------------
Start a new virtual environment:
```
$ pipenv shell
```

<br/>

Install Dependencies
------------
```
$ pipenv install
```


<br/><br/>

**General Config**
==================

There is a config file for general settings: `settings/config.py`. You can place default values there or pass them as script arguments like: 
```sh
python accumulate_coins.py --sleep=35
```

To see available arguments: 
```sh
$ python accumulate_coins.py -h
```


<br/><br/>

**Strategies**
==============

The `strategies/config.py` file is used to configure the strategies that are goinig to be evaluated in order to buy a given pair. For example:
```
    "BNBUSDT": {
        BelowRSI: {
            "period": 14,
            "limit": 20,
            "timeframe": KLINE_INTERVAL_30MINUTE,
            "amount": 20,
            "max_period": 15,  # Minimum amount of periods
        },
    }
```
It will: buy BNB if the current 30-Mins candle RSI-14 is lower than 20.

from binance.enums import *
from strategies.below_rsi import BelowRSI

config = {
    'BTC' : {
        BelowRSI : {
            'period': 14,
            'limit': 20,
            'timeframe': KLINE_INTERVAL_30MINUTE,
            'amount': 50,
        },
    },
}

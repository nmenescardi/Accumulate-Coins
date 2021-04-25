from binance.enums import *
from strategies.below_rsi import BelowRSI

config = {
    'BNBUSDT' : {
        BelowRSI : {
            'period': 14,
            'limit': 20,
            'timeframe': KLINE_INTERVAL_30MINUTE,
            'amount': 10,
            'max_period': 15,  # Minimum amount of periods
        },
    },
}

from binance.enums import KLINE_INTERVAL_30MINUTE  # type: ignore

from strategies.below_rsi import BelowRSI

config = {
    "BNBUSDT": {
        BelowRSI: {
            "period": 14,
            "limit": 27,
            "timeframe": KLINE_INTERVAL_30MINUTE,
            "amount": 15,
            "max_period": 15,
        },
    },
    "BTCUSDT": {
        BelowRSI: {
            "period": 14,
            "limit": 26,
            "timeframe": KLINE_INTERVAL_30MINUTE,
            "amount": 30,
            "max_period": 15,
        },
    },
    "ETHUSDT": {
        BelowRSI: {
            "period": 14,
            "limit": 24,
            "timeframe": KLINE_INTERVAL_30MINUTE,
            "amount": 20,
            "max_period": 15,
        },
    },
    "ADAUSDT": {
        BelowRSI: {
            "period": 14,
            "limit": 26,
            "timeframe": KLINE_INTERVAL_30MINUTE,
            "amount": 20,
            "max_period": 15,
        },
    },
}

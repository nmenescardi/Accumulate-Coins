from binance.enums import KLINE_INTERVAL_1HOUR  # type: ignore

from strategies.below_rsi import BelowRSI

factor = 1

config = {
    "BNBUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 26,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 25 * factor,
            "max_period": 31,
        },
    },
    "BTCUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 30,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 500 * factor,
            "max_period": 31,
        },
    },
    "ETHUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 29,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 300 * factor,
            "max_period": 31,
        },
    },
    "ADAUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 26,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 25 * factor,
            "max_period": 31,
        },
    },
    # "ATOMUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 24,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 25 * factor,
    #         "max_period": 31,
    #     },
    # },
    "DOTUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 26,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 25 * factor,
            "max_period": 31,
        },
    },
    # "FTMUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 24,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 25 * factor,
    #         "max_period": 31,
    #     },
    # },
    "LINKUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 31,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50 * factor,
            "max_period": 31,
        },
    },
    "MATICUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 29,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 25 * factor,
            "max_period": 31,
        },
    },
    "SOLUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 29,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 25 * factor,
            "max_period": 31,
        },
    },
    # "QTUMUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 24,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 5 * factor,
    #         "max_period": 31,
    #     },
    # },
    # "UNIUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 24,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 5 * factor,
    #         "max_period": 31,
    #     },
    # },
    # "VETUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 24,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 25 * factor,
    #         "max_period": 31,
    #     },
    # },
    "XRPUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 29,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50 * factor,
            "max_period": 31,
        },
    },
    # "ZRXUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 24,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 25 * factor,
    #         "max_period": 31,
    #     },
    # },
    "TRXUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 31,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 25 * factor,
            "max_period": 31,
        },
    },
    # "RENUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 24,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 10 * factor,
    #         "max_period": 31,
    #     },
    # },
}

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
            "limit_price_percentage": 0.02, # 2 percent
        },
    },
    "BTCUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 30,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 500 * factor,
            "max_period": 31,
            "limit_price_percentage": 0.02,
        },
    },
    "ETHUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 29,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 300 * factor,
            "max_period": 31,
            "limit_price_percentage": 0.02,
        },
    },
    "ADAUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 26,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 25 * factor,
            "max_period": 31,
            "limit_price_percentage": 0.02,
        },
    },
    # "ATOMUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 24,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 25 * factor,
    #         "max_period": 31,
    #         "limit_price_percentage": 0.02,
    #     },
    # },
    "DOTUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 26,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 25 * factor,
            "max_period": 31,
            "limit_price_percentage": 0.02,
        },
    },
    # "FTMUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 24,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 25 * factor,
    #         "max_period": 31,
    #         "limit_price_percentage": 0.02,
    #     },
    # },
    "LINKUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 31,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 100 * factor,
            "max_period": 31,
            "limit_price_percentage": 0.02,
        },
    },
    "MATICUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 29,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50 * factor,
            "max_period": 31,
            "limit_price_percentage": 0.02,
        },
    },
    "SOLUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 29,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 100 * factor,
            "max_period": 31,
            "limit_price_percentage": 0.02,
        },
    },
    # "QTUMUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 24,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 5 * factor,
    #         "max_period": 31,
    #         "limit_price_percentage": 0.02,
    #     },
    # },
    # "UNIUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 24,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 5 * factor,
    #         "max_period": 31,
    #         "limit_price_percentage": 0.02,
    #     },
    # },
    # "VETUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 24,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 25 * factor,
    #         "max_period": 31,
    #         "limit_price_percentage": 0.02,
    #     },
    # },
    "XRPUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 29,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50 * factor,
            "max_period": 31,
            "limit_price_percentage": 0.02,
        },
    },
    # "ZRXUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 24,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 25 * factor,
    #         "max_period": 31,
    #         "limit_price_percentage": 0.02,
    #     },
    # },
    "TRXUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 31,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 25 * factor,
            "max_period": 31,
            "limit_price_percentage": 0.02,
        },
    },
}

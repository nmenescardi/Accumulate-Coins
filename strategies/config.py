from binance.enums import KLINE_INTERVAL_1HOUR  # type: ignore

from strategies.below_rsi import BelowRSI

factor = 1

config = {
    "BTCUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 28,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 500 * factor,
            "max_period": 31,
            "limit_price_percentage": 0.04,
        },
    },
    "BNBUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 26,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 25 * factor,
            "max_period": 31,
            "limit_price_percentage": 0.04, # 3 percent
        },
    },
    "ETHUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 27,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 300 * factor,
            "max_period": 31,
            "limit_price_percentage": 0.04,
        },
    },
    "ADAUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 27,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 25 * factor,
            "max_period": 31,
            "limit_price_percentage": 0.03,
        },
    },
    # "ATOMUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 24,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 25 * factor,
    #         "max_period": 31,
    #         "limit_price_percentage": 0.03,
    #     },
    # },
    "DOTUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 28,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 25 * factor,
            "max_period": 31,
            "limit_price_percentage": 0.03,
        },
    },
    # "FTMUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 24,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 25 * factor,
    #         "max_period": 31,
    #         "limit_price_percentage": 0.03,
    #     },
    # },
    "LINKUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 28,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 100 * factor,
            "max_period": 31,
            "limit_price_percentage": 0.04,
        },
    },
    # "MATICUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 27,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 50 * factor,
    #         "max_period": 31,
    #         "limit_price_percentage": 0.03,
    #     },
    # },
    "SOLUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 27,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 200 * factor,
            "max_period": 31,
            "limit_price_percentage": 0.03,
        },
    },
    # "QTUMUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 24,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 5 * factor,
    #         "max_period": 31,
    #         "limit_price_percentage": 0.03,
    #     },
    # },
    # "UNIUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 24,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 5 * factor,
    #         "max_period": 31,
    #         "limit_price_percentage": 0.03,
    #     },
    # },
    # "VETUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 24,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 25 * factor,
    #         "max_period": 31,
    #         "limit_price_percentage": 0.03,
    #     },
    # },
    "XRPUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 27,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50 * factor,
            "max_period": 31,
            "limit_price_percentage": 0.04,
        },
    },
    # "ZRXUSDT": {
    #     BelowRSI: {
    #         "period": 30,
    #         "limit": 24,
    #         "timeframe": KLINE_INTERVAL_1HOUR,
    #         "amount": 25 * factor,
    #         "max_period": 31,
    #         "limit_price_percentage": 0.03,
    #     },
    # },
    "TRXUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 26,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50 * factor,
            "max_period": 31,
            "limit_price_percentage": 0.03,
        },
    },
}

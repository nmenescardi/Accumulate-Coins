from binance.enums import KLINE_INTERVAL_1HOUR  # type: ignore

from strategies.below_rsi import BelowRSI

factor = 1

config = {
    "BNBUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 30,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50 * factor,
            "max_period": 35,
        },
    },
    "BTCUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 28,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 500 * factor,
            "max_period": 35,
        },
    },
    "ETHUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 30,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 500 * factor,
            "max_period": 35,
        },
    },
    "ADAUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 28,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50 * factor,
            "max_period": 35,
        },
    },
    "ATOMUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 30,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50 * factor,
            "max_period": 35,
        },
    },
    "DOTUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 28,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50 * factor,
            "max_period": 35,
        },
    },
    "FTMUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 30,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50 * factor,
            "max_period": 35,
        },
    },
    "LINKUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 31,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 100 * factor,
            "max_period": 35,
        },
    },
    "MATICUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 31,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 100 * factor,
            "max_period": 35,
        },
    },
    "QTUMUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 31,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 100 * factor,
            "max_period": 35,
        },
    },
    "UNIUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 27,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 25 * factor,
            "max_period": 35,
        },
    },
    "VETUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 30,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 100 * factor,
            "max_period": 35,
        },
    },
    "XRPUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 28,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 25 * factor,
            "max_period": 35,
        },
    },
    "ZRXUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 28,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 100 * factor,
            "max_period": 35,
        },
    },
    "TRXUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 31,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50 * factor,
            "max_period": 35,
        },
    },
    "RENUSDT": {
        BelowRSI: {
            "period": 30,
            "limit": 28,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 25 * factor,
            "max_period": 35,
        },
    },
}

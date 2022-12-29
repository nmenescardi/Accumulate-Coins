from binance.enums import KLINE_INTERVAL_1HOUR  # type: ignore

from strategies.below_rsi import BelowRSI

config = {
    "BNBUSDT": {
        BelowRSI: {
            "period": 16,
            "limit": 25,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 100,
            "max_period": 18,
        },
    },
    "BTCUSDT": {
        BelowRSI: {
            "period": 16,
            "limit": 30,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 1000,
            "max_period": 18,
        },
    },
    "ETHUSDT": {
        BelowRSI: {
            "period": 16,
            "limit": 26,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 1000,
            "max_period": 18,
        },
    },
    "ADAUSDT": {
        BelowRSI: {
            "period": 16,
            "limit": 22,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50,
            "max_period": 18,
        },
    },
    "ATOMUSDT": {
        BelowRSI: {
            "period": 16,
            "limit": 23,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50,
            "max_period": 18,
        },
    },
    "DOTUSDT": {
        BelowRSI: {
            "period": 16,
            "limit": 22,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50,
            "max_period": 18,
        },
    },
    "FTMUSDT": {
        BelowRSI: {
            "period": 16,
            "limit": 22,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50,
            "max_period": 18,
        },
    },
    "LINKUSDT": {
        BelowRSI: {
            "period": 16,
            "limit": 25,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50,
            "max_period": 18,
        },
    },
    "MATICUSDT": {
        BelowRSI: {
            "period": 16,
            "limit": 26,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50,
            "max_period": 18,
        },
    },
    "UNIUSDT": {
        BelowRSI: {
            "period": 16,
            "limit": 22,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50,
            "max_period": 18,
        },
    },
    "VETUSDT": {
        BelowRSI: {
            "period": 16,
            "limit": 22,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 50,
            "max_period": 18,
        },
    },
    "XRPUSDT": {
        BelowRSI: {
            "period": 16,
            "limit": 24,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 100,
            "max_period": 18,
        },
    },
    "ZRXUSDT": {
        BelowRSI: {
            "period": 16,
            "limit": 22,
            "timeframe": KLINE_INTERVAL_1HOUR,
            "amount": 100,
            "max_period": 18,
        },
    },
}

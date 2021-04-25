from binance.enums import KLINE_INTERVAL_30MINUTE  # type: ignore

from strategies.below_rsi import BelowRSI

config = {
    "BNBUSDT": {
        BelowRSI: {
            "period": 14,
            "limit": 20,
            "timeframe": KLINE_INTERVAL_30MINUTE,
            "amount": 20,
            "max_period": 15,  # Minimum amount of periods
        },
    },
    "BTCUSDT": {
        BelowRSI: {
            "period": 14,
            "limit": 10,
            "timeframe": KLINE_INTERVAL_30MINUTE,
            "amount": 20,
            "max_period": 15,  # Minimum amount of periods
        },
    },
}

import numpy as np  # type: ignore
import pandas as pd  # type: ignore

from client.client import Client
from helpers.singleton import singleton
from logger.app_logger import AppLogger


@singleton
class Dataframe:
    """ Helper class to create a dataframe from data received by the client """

    def __init__(self):
        self.client = Client().get()
        self.cached_dataframes = {}
        self.logger = AppLogger().get()

    def get(self, symbol, interval, limit=499):
        """ Creates a dataframe from data received by the client """

        candles = self._fetch_candles(symbol=symbol, interval=interval, limit=limit)

        df = pd.DataFrame(
            columns=[
                "open_time",
                "open",
                "high",
                "low",
                "close",
                "volume",
                "close_time",
            ]
        )

        opentime, lopen, lhigh, llow, lclose, lvol, closetime = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )

        for candle in candles:
            opentime.append(candle[0])
            lopen.append(candle[1])
            lhigh.append(candle[2])
            llow.append(candle[3])
            lclose.append(candle[4])
            lvol.append(candle[5])
            closetime.append(candle[6])

        df["open_time"] = opentime
        df["open"] = np.array(lopen).astype(np.float)
        df["high"] = np.array(lhigh).astype(np.float)
        df["low"] = np.array(llow).astype(np.float)
        df["close"] = np.array(lclose).astype(np.float)
        df["volume"] = np.array(lvol).astype(np.float)
        df["close_time"] = closetime
        return df

    def _fetch_candles(self, symbol, interval, limit):
        cache_key = symbol + interval + str(limit)

        if cache_key in self.cached_dataframes:
            self.logger.debug("%s Dataframe fetched from cache", cache_key)
            return self.cached_dataframes[cache_key]

        candles = self.client.get_klines(symbol=symbol, interval=interval, limit=limit)
        self.logger.debug("%s Dataframe fetched from a Client API call", cache_key)
        self.cached_dataframes[cache_key] = candles
        return candles

    def flush_cache(self):
        """ Empty out the entire cache """
        self.cached_dataframes = {}

    def get_quantity(self, df, amount):
        price = df.close.iloc[-1]
        quantity = round(amount / price, 3)
        self.logger.info(
            "price: %s... Quantity to buy: %s.",
            price,
            quantity,
        )
        return quantity



import pandas as pd
import numpy as np

from client.client import Client
from helpers.singleton import singleton


@singleton
class Dataframe:
    
    def __init__(self):
        self.client = Client().get()
        self.cached_dataframes = {}

    def get(self, symbol, interval, limit = 499):        
        candles = self._fetch_candles(symbol=symbol, interval=interval, limit=limit)

        df = pd.DataFrame(columns= ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time'])

        opentime, lopen, lhigh, llow, lclose, lvol, closetime = [], [], [], [], [], [], []

        for candle in candles:
            opentime.append(candle[0])
            lopen.append(candle[1])
            lhigh.append(candle[2])
            llow.append(candle[3])
            lclose.append(candle[4])
            lvol.append(candle[5])
            closetime.append(candle[6])

        df['open_time'] = opentime
        df['open'] = np.array(lopen).astype(np.float)
        df['high'] = np.array(lhigh).astype(np.float)
        df['low'] = np.array(llow).astype(np.float)
        df['close'] = np.array(lclose).astype(np.float)
        df['volume'] = np.array(lvol).astype(np.float)
        df['close_time'] = closetime
        return df

    def _fetch_candles(self, symbol, interval, limit):
        cache_key = symbol + interval + str(limit)
        
        if cache_key in self.cached_dataframes:
            print('fetched from cache') #TODO: logger
            return self.cached_dataframes[ cache_key ]

        else:
            candles = self.client.get_klines(symbol=symbol, interval=interval, limit=limit)
            print('fetched from client')
            self.cached_dataframes[ cache_key ] = candles
            return candles

    def flush_cache(self):
        self.cached_dataframes = {}

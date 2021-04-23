
from strategies.config import config

from client.client import Client

import pandas as pd
import numpy as np


class Manager:
    
    def __init__(self):
        self.client = Client().get()

    def run(self):

        for symbol, strategies in config.items():
            print(symbol)

            for strategy_class, params in strategies.items():
                    
                timeframe = params['timeframe']

                max_period = 14 # TODO: calculate max_period
                
                df = self._get_df(symbol, timeframe) #TODO: cache api response for the same pair/timeframe
                
                strategy = strategy_class(df=df,**params) 
                if strategy.should_buy():
                    #TODO perform api call to place the market order.
                    break

    def _get_df(self, symbol, interval):
        df = pd.DataFrame(columns= ['Open_time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close_time'])

        candles = self.client.get_klines(symbol=symbol, interval=interval)

        opentime, lopen, lhigh, llow, lclose, lvol, closetime = [], [], [], [], [], [], []

        for candle in candles:
            opentime.append(candle[0])
            lopen.append(candle[1])
            lhigh.append(candle[2])
            llow.append(candle[3])
            lclose.append(candle[4])
            lvol.append(candle[5])
            closetime.append(candle[6])

        df['Open_time'] = opentime
        df['Open'] = np.array(lopen).astype(np.float)
        df['High'] = np.array(lhigh).astype(np.float)
        df['Low'] = np.array(llow).astype(np.float)
        df['Close'] = np.array(lclose).astype(np.float)
        df['Volume'] = np.array(lvol).astype(np.float)
        df['Close_time'] = closetime
        return df

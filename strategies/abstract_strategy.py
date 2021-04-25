from abc import ABC, abstractmethod
from binance.enums import *
import pandas_ta as ta
from logger.app_logger import AppLogger


class AbstractStrategy(ABC):
    
    def __init__(self, df, timeframe = KLINE_INTERVAL_1HOUR, amount = 20, **kwargs):
        self.df = df
        self.timeframe = timeframe
        self.ammount = amount
        self.logger = AppLogger().get()

    @abstractmethod
    def should_buy(self):
        pass

from abc import ABC, abstractmethod
from binance.enums import *


class AbstractStrategy(ABC):
    
    def __init__(self, timeframe = KLINE_INTERVAL_1HOUR, amount = 20, **kwargs):
        self.timeframe = timeframe
        self.ammount = amount

    @abstractmethod
    def run(self, df):
        pass

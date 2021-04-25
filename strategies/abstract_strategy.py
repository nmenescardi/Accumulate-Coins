from abc import ABC, abstractmethod

import pandas_ta as ta  # type: ignore  # pylint: disable=E0401, W0611
from binance.enums import KLINE_INTERVAL_1HOUR  # type: ignore

from logger.app_logger import AppLogger


class AbstractStrategy(ABC):
    """ Abstract class to setup common dependencies between strategies """

    def __init__(self, df, timeframe=KLINE_INTERVAL_1HOUR, amount=20, **kwargs):
        self.df = df
        self.timeframe = timeframe
        self.ammount = amount
        self.logger = AppLogger().get()

    @abstractmethod
    def should_buy(self):
        """ Must be implemented by strategies to decide if placing and order or not """

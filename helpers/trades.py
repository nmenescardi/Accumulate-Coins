from datetime import datetime
from helpers.singleton import singleton
from logger.app_logger import AppLogger
from settings.settings import Settings

@singleton
class TradesHelper:

    def __init__(self):
        self.trades = {}
        self.logger = AppLogger().get()
        self.minutes_between_trades = Settings().get("minutes_between_trades")

    def add_trade(self, symbol):
        self.logger.debug("Adding a recent trade for %s", symbol)
        self.trades[symbol] = datetime.now()

    def is_cooling_down(self, symbol):
        self.logger.debug("Checking if %s has a recent trade", symbol)
        last_trade_datetime = self.trades.get(symbol)

        if last_trade_datetime is None:
            return False

        self.logger.debug("Most recent trade for %s is %s", symbol, last_trade_datetime)
        return self._was_recent(last_trade_datetime)

    def _was_recent(self, last_trade_datetime):
        minutes_since_last_trade = (datetime.now() - last_trade_datetime).total_seconds() / 60.0
        
        if self.minutes_between_trades > minutes_since_last_trade:
            self.logger.debug("Last trade is recent. It should cooldown.")
            return True

        self.logger.debug("Last trade is not recent.")
        return False

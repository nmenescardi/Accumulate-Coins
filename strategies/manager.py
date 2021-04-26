import time

from client.client import Client
from helpers.dataframe import Dataframe
from helpers.trades import TradesHelper
from logger.app_logger import AppLogger
from strategies.config import config
from settings.settings import Settings
from wallets.futures import Futures as FuturesWallet
from wallets.spot import Spot as SpotWallet


class Manager:
    """ Manages the process to check a strategy list for each pair declared on config """

    def __init__(self):
        self.client = Client().get()
        self.futures_wallet = FuturesWallet()
        self.spot_wallet = SpotWallet()
        self.dataframe_helper = Dataframe()
        self.logger = AppLogger().get()
        self.trades_helper = TradesHelper()
        self.sleep_between_calls = Settings().get("sleep_between_calls")

    def run(self):
        """ Main entry point to handle the process """

        while True:
            for symbol, strategies in config.items():
                time.sleep(self.sleep_between_calls)

                # Avoids re-buying same symbol in a short period of time
                if self.trades_helper.is_cooling_down(symbol):
                    continue  # to the next symbol
                
                self.logger.info("Running strategies for: %s", symbol)
                self.dataframe_helper.flush_cache()

                for strategy_class, params in strategies.items():

                    timeframe = params["timeframe"]
                    amount = params["amount"]
                    max_period = params["max_period"]

                    df = self.dataframe_helper.get(symbol, timeframe, limit=max_period)

                    strategy = strategy_class(df=df, **params)

                    if strategy.should_buy():
                        strategy_name = strategy.__class__.__name__
                        self.logger.info(
                            "Buy signal for %s using the %s strategy",
                            symbol,
                            strategy_name,
                        )

                        self.futures_wallet.transfer_to_spot(amount=amount)

                        price = df.close.iloc[-1]
                        quantity = round(amount / price, 3)
                        self.logger.info(
                            "%s price: %s... Quantity to buy: %s.",
                            symbol,
                            price,
                            quantity,
                        )

                        was_placed = self.spot_wallet.place_order(
                            symbol=symbol, quantity=quantity
                        )

                        if was_placed:
                            self.trades_helper.add_trade(symbol)

                        break # to the next symbol
                time.sleep(self.sleep_between_calls)

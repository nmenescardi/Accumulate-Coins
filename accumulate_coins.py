"""Script for transfering funds from the Binance futures wallets into spot and accumulate coins."""

import sys

from binance.exceptions import BinanceAPIException  # type: ignore

from client.client import Client
from logger.app_logger import AppLogger
from settings.settings import Settings
from wallets.futures import Futures as FuturesWallet
from wallets.spot import Spot as SpotWallet


class AccumulateCoins:
    """ Main class to control the process """

    def __init__(self):
        self.logger = AppLogger().get()
        self.settings = Settings().get()
        self.client = Client().get()
        self.futures_wallet = FuturesWallet()
        self.spot_wallet = SpotWallet()

    def _print_balance(self):
        self.futures_wallet.print_balance()
        self.spot_wallet.print_balance()

    def transfer(self):
        amount = self.settings["tx_amount"]
        self.logger.info("Amount to transfer %s", amount)

        if amount > self.futures_wallet.get_balance():
            self.logger.warning("Insufficient balance.")
            sys.exit()
        else:
            try:
                self.client.futures_account_transfer(
                    asset="USDT", amount=amount, type=2, timestamp=2348273489823
                )
                self.logger.info("Balance transfer succesful !!!")
            except BinanceAPIException as error:
                self.logger.error("There was an API error: %s", error)

    def run(self):
        """Main entry point"""
        self._print_balance()
        self.transfer()
        self._print_balance()


if __name__ == "__main__":
    AccumulateCoins().run()

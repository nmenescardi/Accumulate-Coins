"""Script for transfering funds from the Binance futures wallets into spot and accumulate coins."""

from binance.exceptions import BinanceAPIException  # type: ignore

from client.client import Client
from logger.app_logger import AppLogger
from wallets.futures import Futures as FuturesWallet
from wallets.spot import Spot as SpotWallet


class AccumulateCoins:
    """ Main class to control the process """

    def __init__(self):
        self.client = Client().get()
        self.logger = AppLogger().get()
        self.futures_wallet = FuturesWallet()
        self.spot_wallet = SpotWallet()

    def _print_balance(self):
        self.futures_wallet.print_balance()
        self.spot_wallet.print_balance()

    def _get_value(self):
        value = input("Enter the value to transfer from Futures to spot wallet: ")

        if value > self.futures_wallet.get_balance():
            self.logger.warning("Insufficient balance, Enter the values again.")
            self._get_value()
        else:
            try:
                self.client.futures_account_transfer(
                    asset="USDT", amount=value, type=2, timestamp=2348273489823
                )
                self.logger.info("Balance transfer succesful !!!")
            except BinanceAPIException as error:
                self.logger.error("There was an API error: %s", error)

    def run(self):
        """Main entry point"""
        self._print_balance()
        self._get_value()
        self._print_balance()


if __name__ == "__main__":
    AccumulateCoins().run()

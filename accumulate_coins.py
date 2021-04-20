"""Script for transfering funds from the Binance futures wallets into spot and accumulate coins."""

from binance.exceptions import BinanceAPIException  # type: ignore

from client.client import Client
from logger.app_logger import AppLogger


class AccumulateCoins:
    """ Main class to control the process """

    def __init__(self):
        self.client = Client().get()
        self.logger = AppLogger().get()

    def _get_usdt_futures_balance(self):
        details = self.client.futures_account_balance()
        for i in details:
            if i["asset"] == "USDT":
                return i["balance"]
        return 0

    def _get_usdt_spot_balance(self):
        details = self.client.get_account()
        balance_details = details["balances"]
        for i in balance_details:
            if i["asset"] == "USDT":
                return i["free"]
        return 0

    def _print_balance(self):
        self.logger.info("Spot Balance in USDT is: %s", self._get_usdt_spot_balance())
        self.logger.info(
            "Futures Balance in USDT is: %s", self._get_usdt_futures_balance()
        )

    def _get_value(self):
        value = input("Enter the value to transfer from Futures to spot wallet: ")

        if value > self._get_usdt_futures_balance():
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

"""Script for transfering funds from the Binance futures wallets into spot and accumulate coins."""

from wallets.futures import Futures as FuturesWallet
from wallets.spot import Spot as SpotWallet
from strategies.manager import Manager as StrategiesManager


class AccumulateCoins:
    """ Main class to control the process """

    def __init__(self):
        self.futures_wallet = FuturesWallet()
        self.spot_wallet = SpotWallet()
        self.strategies_manager = StrategiesManager()

    def _print_balance(self):
        self.futures_wallet.print_balance()
        self.spot_wallet.print_balance()

    def run(self):
        """Main entry point"""
        self._print_balance()
        self.strategies_manager.run()
        self._print_balance()


if __name__ == "__main__":
    AccumulateCoins().run()

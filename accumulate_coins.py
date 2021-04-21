"""Script for transfering funds from the Binance futures wallets into spot and accumulate coins."""

from wallets.futures import Futures as FuturesWallet
from wallets.spot import Spot as SpotWallet


class AccumulateCoins:
    """ Main class to control the process """

    def __init__(self):
        self.futures_wallet = FuturesWallet()
        self.spot_wallet = SpotWallet()

    def _print_balance(self):
        self.futures_wallet.print_balance()
        self.spot_wallet.print_balance()

    def run(self):
        """Main entry point"""
        self._print_balance()
        self.futures_wallet.transfer_to_spot()
        self._print_balance()


if __name__ == "__main__":
    AccumulateCoins().run()

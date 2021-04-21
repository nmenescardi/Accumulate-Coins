"""Spot wallet"""

from wallets.abstract_wallet import AbstractWallet


class Spot(AbstractWallet):
    """Spot wallet"""

    def get_balance(self):
        details = self.client.get_account()
        balance_details = details["balances"]
        for i in balance_details:
            if i["asset"] == "USDT":
                return i["free"]
        return 0.0

    def print_balance(self):
        self.logger.info("Spot Balance in USDT is: %s", self.get_balance())

"""Futures wallet"""


from wallets.abstract_wallet import AbstractWallet


class Futures(AbstractWallet):
    """Futures wallet"""

    def get_balance(self):
        details = self.client.futures_account_balance()
        for i in details:
            if i["asset"] == "USDT":
                return float(i["balance"])
        return 0.0

    def print_balance(self):
        self.logger.info("Futures Balance in USDT is: %s", self.get_balance())

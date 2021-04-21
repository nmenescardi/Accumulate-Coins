"""Futures wallet"""

from binance.exceptions import BinanceAPIException  # type: ignore

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

    def transfer_to_spot(self):
        amount = self.settings["tx_amount"]
        self.logger.info("Amount to transfer %s", amount)

        if amount > self.get_balance():
            self.logger.warning("Insufficient balance.")
            return
        else:
            try:
                self.client.futures_account_transfer(
                    asset="USDT", amount=amount, type=2, timestamp=2348273489823
                )
                self.logger.info("Balance transfer succesful !!!")
            except BinanceAPIException as error:
                self.logger.error("There was an API error: %s", error)

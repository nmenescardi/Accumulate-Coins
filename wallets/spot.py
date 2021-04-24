"""Spot wallet"""

from wallets.abstract_wallet import AbstractWallet

from binance.exceptions import BinanceAPIException


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

    def place_order(self, symbol, quantity):
        try:
            self.logger.debug('Placing an order for %s', symbol)
            order = self.client.order_market_buy(
                symbol=symbol,
                quantity=quantity
            )
            self.logger.info('An order was placed of %s qty for %s.', str(quantity), symbol)
            self.logger.debug('The order: %s', order)
        except BinanceAPIException as error:
            self.logger.error('An API Exception occurred: %s', error)

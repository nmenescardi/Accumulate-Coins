"""Spot wallet"""

from binance.exceptions import BinanceAPIException  # type: ignore

from wallets.abstract_wallet import AbstractWallet

import math

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
        """ Places a market order on the Spot wallet """
        try:
            self.logger.debug("Placing an order for %s", symbol)
            order = self.client.order_market_buy(symbol=symbol, quantity=quantity)
            self.logger.info(
                "An order was placed of %s qty for %s.", str(quantity), symbol
            )
            self.logger.debug("The order: %s", order)
            was_placed = True
        except BinanceAPIException as error:
            self.logger.error("An API Exception occurred: %s", error)
            was_placed = False

        return was_placed

    def get_quantity(self, price, amount, symbol):
        """ calculates quantity to buy based on last price and the given amount """

        self.logger.debug('getting quantity for %s', symbol)
        step_size = self._get_step_size(symbol=symbol)
        
        base_quantity = (amount / price) * 0.9995
        precision = int(round(-math.log(step_size, 10), 0))
        quantity = float(round(base_quantity, precision))
        
        self.logger.debug(
            '%s final Quantity: %s... Precision: %s... Base Qty: %s... ', 
            symbol, 
            quantity, 
            precision, 
            base_quantity
        )
        return quantity

    def _get_step_size(self, symbol):
        step_size = self._get_from_symbol_info_filters(symbol, 'LOT_SIZE') or 0.0001
        return float(step_size)

    def _get_from_symbol_info_filters(self, symbol, filter_type):
        sym_info = self.client.get_symbol_info(symbol)
        filters = sym_info['filters']
        for f in filters:
            if f['filterType'] == filter_type:
                return f['stepSize']

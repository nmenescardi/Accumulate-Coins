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

    def get_quantity(self, price, original_amount, symbol):
        """ calculates quantity to buy based on last price and the given amount """

        self.logger.debug('getting quantity for %s', symbol)
        step_size = self._get_step_size(symbol=symbol)

        base_fee = self.client.get_trade_fee(symbol=symbol)[0]['takerCommission'] or 0.001
        fee = (100 - float(base_fee)) / 100
        
        min_notional = self._get_min_notional(symbol=symbol)
        amount = original_amount if original_amount >= min_notional else min_notional * 1.01 

        base_quantity = (amount / price) * fee
        precision = int(round(-math.log(step_size, 10), 0))
        quantity = float(round(base_quantity, precision))

        self.logger.debug(
            '%s Final Qty: %s.. Precision: %s.. Base Qty: %s.. Base Fee: %s.. Fee: %s.. Final Amount: %s.. Original Amount: %s.. MIN Notional: %s',
            symbol,
            quantity,
            precision,
            base_quantity,
            base_fee,
            fee,
            amount,
            original_amount,
            min_notional
        )
        return quantity

    def _get_min_notional(self, symbol):
        min_notional = self._get_from_symbol_info_filters(symbol, 'MIN_NOTIONAL', 'minNotional') or 11
        return float(min_notional)

    def _get_step_size(self, symbol):
        step_size = self._get_from_symbol_info_filters(symbol, 'LOT_SIZE', 'stepSize') or 0.0001
        return float(step_size)

    def _get_from_symbol_info_filters(self, symbol, filter_type, prop):
        sym_info = self.client.get_symbol_info(symbol)
        filters = sym_info['filters']
        for f in filters:
            if f['filterType'] == filter_type:
                return f[prop]

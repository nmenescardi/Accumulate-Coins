
import time
from strategies.config import config

from client.client import Client

from wallets.futures import Futures as FuturesWallet
from wallets.spot import Spot as SpotWallet
from logger.app_logger import AppLogger
from helpers.dataframe import Dataframe

class Manager:
    
    def __init__(self):
        self.client = Client().get()
        self.futures_wallet = FuturesWallet()
        self.spot_wallet = SpotWallet()
        self.dataframe_helper = Dataframe()
        self.logger = AppLogger().get()

    def run(self):

        while True:
            for symbol, strategies in config.items():
                self.logger.info("Running strategies for: %s", symbol)
                self.dataframe_helper.flush_cache()

                for strategy_class, params in strategies.items():

                    timeframe = params['timeframe']
                    amount  = params['amount']
                    max_period  = params['max_period']

                    df = self.dataframe_helper.get(symbol, timeframe, limit = max_period)

                    strategy = strategy_class(df=df,**params) 

                    if strategy.should_buy():
                        strategy_name = strategy.__class__.__name__
                        self.logger.info("Buy signal for %s using the %s strategy", symbol, strategy_name)

                        self.futures_wallet.transfer_to_spot(amount=amount)

                        try:
                            price = df.close.iloc[-1]
                            quantity = round(amount / price, 3)
                            self.logger.info("%s price: %s... Quantity to buy: %s.", symbol, price, quantity)

                            self.spot_wallet.place_order(symbol=symbol, quantity=quantity)
                        except Exception as error:
                            self.logger.error("There was a general error: %s", error)

                        #TODO: Add coldown for that pair
                        break
    
                time.sleep(15)

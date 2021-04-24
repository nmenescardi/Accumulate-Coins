
from strategies.config import config

from client.client import Client

from wallets.futures import Futures as FuturesWallet
from wallets.spot import Spot as SpotWallet

from helpers.dataframe import Dataframe

class Manager:
    
    def __init__(self):
        self.client = Client().get()
        self.futures_wallet = FuturesWallet()
        self.spot_wallet = SpotWallet()
        self.dataframe_helper = Dataframe()

    def run(self):

        for symbol, strategies in config.items():
            print(symbol)
            
            self.dataframe_helper.flush_cache()

            for strategy_class, params in strategies.items():

                timeframe = params['timeframe']
                amount  = params['amount']
                max_period  = params['max_period']

                df = self.dataframe_helper.get(symbol, timeframe, limit = max_period)

                strategy = strategy_class(df=df,**params) 

                if strategy.should_buy():                    
                    self.futures_wallet.transfer_to_spot(amount=amount)

                    price = df.Close.iloc[-1]
                    quantity = round(amount / price, 3)
                    self.spot_wallet.place_order(symbol=symbol, quantity=quantity)

                    return


from strategies.config import config

from binance.exceptions import BinanceAPIException
from client.client import Client

from wallets.futures import Futures as FuturesWallet
from wallets.spot import Spot as SpotWallet

from helpers.dataframe import Dataframe

class Manager:
    
    def __init__(self):
        self.client = Client().get()
        self.futures_wallet = FuturesWallet()
        self.dataframe_helper = Dataframe()

    def run(self):

        for symbol, strategies in config.items():
            print(symbol)

            for strategy_class, params in strategies.items():

                timeframe = params['timeframe']

                amount  = params['amount']

                max_period = 14 # TODO: calculate max_period

                df = self.dataframe_helper.get(symbol, timeframe)                          

                strategy = strategy_class(df=df,**params) 

                if strategy.should_buy():                    
                    try:     
                        self.futures_wallet.transfer_to_spot(amount=amount)

                        price = df.Close.iloc[-1]
                        quantity = round(amount / price, 4)

                        order = self.client.order_market_buy(
                            symbol=symbol,
                            quantity=quantity
                        )
                        print(order)
                    except BinanceAPIException as e:
                        print(e)

                    return



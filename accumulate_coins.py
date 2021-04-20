from binance.client import Client
from binance.exceptions import BinanceAPIException
import os


class AccumulateCoins:
    def __init__(self):
        self.client = Client(os.getenv("BINANCE_API"), os.getenv("BINANCE_SECRET"))

    def get_usdt_futures_balance(self):
        details = self.client.futures_account_balance()
        for i in details:
            if i["asset"] == "USDT":
                return i["balance"]

    def get_usdt_spot_balance(self):
        details = self.client.get_account()
        balance_details = details["balances"]
        for i in balance_details:
            if i["asset"] == "USDT":
                return i["free"]

    def print_balance(self):
        print("Spot Balance in USDT is: ", self.get_usdt_spot_balance())
        print("Futures Balance in USDT is: ", self.get_usdt_futures_balance())

    def get_value(self):
        value = input("Enter the value to transfer from Futures to spot wallet: ")

        if value > self.get_usdt_futures_balance():
            print("Insufficient balance, Enter the values again.")
            self.get_value()
        else:
            try:
                self.client.futures_account_transfer(
                    asset="USDT", amount=value, type=2, timestamp=2348273489823
                )
                print("Balance transfer succesful !!!")
            except BinanceAPIException as error:
                pass

    def run(self):
        self.print_balance()
        self.get_value()
        self.print_balance()


if __name__ == "__main__":
    AccumulateCoins().run()

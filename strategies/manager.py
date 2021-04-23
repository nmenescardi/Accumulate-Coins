
from strategies.config import config


class Manager:
    
    def run(self):

        for coin, strategies in config.items():
            print(coin)
            
            strategies_to_run = []
            
            for strategy_class, params in strategies.items():
                
                strategies_to_run.append( 
                    strategy_class(**params) 
                )
                
            max_period = 14 # TODO: calculate max_period
            
            df = None #TODO: perform api call to get coin df using max_period
            
            for strategy in strategies_to_run:
                should_buy = strategy.run(df)
                
                if should_buy:
                    #TODO perform api call to place the market order.
                    break

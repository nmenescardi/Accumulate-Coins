
from strategies.abstract_strategy import AbstractStrategy


class BelowRSI(AbstractStrategy):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        print(kwargs)

    def run(self, df):
        print(self)

from strategies.abstract_strategy import AbstractStrategy


class BelowRSI(AbstractStrategy):
    """ Buying if rsi value is below a given limit """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.period = kwargs["period"]
        self.limit = kwargs["limit"]

    def should_buy(self):
        rsi_series = self.df.ta.rsi(append=True, length=self.period)
        rsi_value = rsi_series.iloc[-1]

        self.logger.info(
            "RSI Period: %s ---  RSI Value: %s ---  Limit: %s",
            self.period,
            rsi_value,
            self.limit,
        )

        if rsi_value <= self.limit:
            return True

        return False

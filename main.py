# region imports
from AlgorithmImports import *
# endregion

class QuantLeague(QCAlgorithm):
    def initialize(self):
        self.set_start_date(2020, 1, 1)
        self.set_cash(1000000)
        self.symbol = self.add_equity("SPY", Resolution.Daily).Symbol
        self.fast_moving_average = self.sma(self.symbol, 50, Resolution.Daily)
        self.last_action = None

    def on_data(self, data):
        # Ensure we have enough data to calculate the moving average
        if not self.fast_moving_average.is_ready:
            return
        
        price = data[self.symbol].Close
        # Buy if the price is above the moving average
        if price > self.fast_moving_average.current.value:
            if not self.portfolio.invested or self.last_action == "Sell":
                self.set_holdings(self.symbol, 1)
                self.last_action = "Buy"

        # Sell if the price is below the moving average
        elif price < self.fast_moving_average.current.value:
            if self.portfolio.invested and self.last_action == "Buy":
                self.liquidate(self.symbol)
                self.last_action = "Sell"
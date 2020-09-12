from HistoricDataCollector import HistoricDataCollector
from pandas_datareader._utils import RemoteDataError


class EarningsProfitCalculator(object):
    def __init__(self, price_minimum=0):
        self.profits = []
        self.price_minimum = price_minimum
        self.profitable_trades = 0
        self.unprofitable_trades = 0

    def manage_profit(self, profit):
        self.profits.append(profit)
        if profit > 0:
            self.profitable_trades += 1
        else:
            self.unprofitable_trades += 1

    def add_earning(self, earning, buy_on, sell_on):
        symbol, date = earning.symbol, earning.date
        earning.buy_date = date.minus_days(buy_on)
        earning.sell_date = date.minus_days(sell_on)
        try:
            earning.buy_price = HistoricDataCollector.get_close_price_for_symbol_on_day(symbol, earning.buy_date)
            if earning.buy_price is not None:
                if earning.buy_price < self.price_minimum:
                    print("Price too low, ignoring!")
                    return None
                earning.sell_price = HistoricDataCollector.get_close_price_for_symbol_on_day(symbol, earning.sell_date)
                if earning.sell_price is not None:
                    earning.profit = 1.0 - (earning.buy_price / earning.sell_price)
                    self.manage_profit(earning.profit)
        except RemoteDataError:
            print("Could not gather data for {}, ignoring in calculations!".format(symbol))

    def compute_average_profit(self):
        if len(self.profits) != 0:
            return sum(self.profits) / len(self.profits)

    def compute_profitability(self):
        if self.unprofitable_trades + self.profitable_trades != 0:
            return self.profitable_trades / (self.profitable_trades + self.unprofitable_trades)

    def print_stats(self):
        print("\nAverage profit: {}\nTotal Profitability Percentage: {}%".format(
            str(self.compute_average_profit()),
            str(self.compute_profitability())
        ))

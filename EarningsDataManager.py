from yahoo_earnings_calendar import YahooEarningsCalendar
from DatePickHelper import DatePickHelper


class EarningsData(object):
    def __init__(self, data_dict):
        self.symbol = data_dict["ticker"]
        self.date = DatePickHelper.earning_string_to_date(data_dict["startdatetime"])
        self.buy_price = None
        self.buy_date = None
        self.sell_price = None
        self.sell_date = None
        self.profit = None
        # BMO - Before Market Open, # AMC - After Market Close , # TNC - No Data
        self.release_time = data_dict["startdatetimetype"]

    def to_string(self):
        return "{} {} {}".format(self.symbol, self.release_time, self.date.to_string())


class EarningsDataManager(object):
    @staticmethod
    def get_earnings_for_days(date_from, date_to):
        try:
            calender_manager = YahooEarningsCalendar()
            data = calender_manager.earnings_between(date_from, date_to)
            return [EarningsData(i) for i in data]
        except KeyError:
            return []

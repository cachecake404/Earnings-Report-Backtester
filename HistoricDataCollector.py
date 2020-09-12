from pandas_datareader.data import DataReader


# A class that is responsible for collecting historic data.
class HistoricDataCollector(object):
    # Returns the closing price for a given day for a given stock
    @staticmethod
    def get_close_price_for_symbol_on_day(symbol, day):
        counter = 0
        while counter < 5:
            day_name_today = day.to_date().strftime("%A")
            try:
                if day_name_today == "Sunday" or day_name_today == "Saturday":
                    day = day.minus_days(1)
                else:
                    return float(DataReader(symbol, 'yahoo', day.to_string(), day.to_string())["Close"])
            except KeyError:
                counter += 1
                day = day.minus_days(1)
                day_name_yesterday = day.to_date().strftime("%A")
                print("Could not find any data for {} on {} looking for data from before {}!".format
                      (symbol, day_name_today, day_name_yesterday))
        print("Failed to find any data for {}!".format(symbol))
        return None

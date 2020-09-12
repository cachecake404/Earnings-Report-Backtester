from datetime import datetime, timedelta


class DateDataWrapper(object):
    def __init__(self, date):
        self.date = date

    def minus_days(self, days):
        return DatePickHelper.minus_days_from_date(self.date, days)

    def to_string(self, split_date_string="-"):
        return self.date.strftime('%Y{}%m{}%d'.format(split_date_string, split_date_string))

    def to_date(self):
        return self.date


class DatePickHelper(object):
    @staticmethod
    def get_today():
        return DateDataWrapper(datetime.today())

    @staticmethod
    def minus_days_from_today(days_to_subtract):
        return DateDataWrapper((datetime.today() - timedelta(days=days_to_subtract)))

    @staticmethod
    def minus_days_from_date(date_custom, days_to_subtract):
        return DateDataWrapper((date_custom - timedelta(days=days_to_subtract)))

    @staticmethod
    def earning_string_to_date(date_string):
        date_string_parsed = date_string.split("T")[0]
        return DateDataWrapper(datetime.strptime(date_string_parsed, '%Y-%m-%d'))

from DatePickHelper import DatePickHelper
from EarningsDataManager import EarningsDataManager
from EarningsProfitCalculator import EarningsProfitCalculator

# Will look at all past earnings "total_earnings" days from today
total_earnings = 15
# Will sell stock "days_before_earnings_sell" days before earnings.
days_before_earnings_sell = 1
# Will buy stock "days_before_earnings_buy" days before earnings
days_before_earnings_buy = 7 

earnings_from_date = DatePickHelper.minus_days_from_today(total_earnings)
earnings_to_date = DatePickHelper.minus_days_from_today(0)

print("Loading earnings data! Please Wait!\n")
earning_calculator = EarningsProfitCalculator()
earning_data = EarningsDataManager.get_earnings_for_days(earnings_from_date.to_date(), earnings_to_date.to_date())
print("Done loading earnings data!\n")

for earning in earning_data:
    print("Checking earnings for {} on {}: ".format(earning.symbol, earning.date.to_string()))
    earning_calculator.add_earning(earning, days_before_earnings_buy, days_before_earnings_sell)
    if earning.buy_price is not None and earning.sell_price is not None:
        print("Bought {} at {} on {} and sold at {} on {} for a total profit of {}%".format(
            earning.symbol,
            str(earning.buy_price),
            earning.buy_date.to_string(),
            str(earning.sell_price),
            earning.sell_date.to_string(),
            str(earning.profit)))
        earning_calculator.print_stats()
    print("------------------------------------------------\n")

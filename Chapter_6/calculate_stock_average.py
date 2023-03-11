import datetime
def middle(stock, date):
    symbol, current, high, low = stock
    return ((high + low) / 2, date)

mid_value, date = middle(("GOOG", 613.30, 625.86, 610.50),datetime.date(2010, 1, 6))

stock = "GOOG",  613.30, 625.86, 610.50
high = stock[2]
print(high)

print(stock[1:3])

from collections import namedtuple
Stock = namedtuple("Stock", "symbol current high low")
stock = Stock('GOOG', 613.30, high=625.86, low=610.50)
print(stock.high)
symbol, current, high, low = stock
print(current)
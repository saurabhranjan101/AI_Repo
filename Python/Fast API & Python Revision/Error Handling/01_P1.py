revenue = 0
expense = 10
try:
    profit = revenue - expense
    margin = profit * 100/revenue
    print(margin)
except ZeroDivisionError:
    print("Revenue cannot be Zero")
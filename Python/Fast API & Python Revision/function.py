def calculate_margin(revenue:float, expenses:float) -> float: ##:float -- this is hint
    profit = revenue - expenses
    margin = profit * 100/revenue
    return margin, profit
a, b =  calculate_margin(200, 75)
print(f"Margin is {a} and Profit is {b}")

def calculate_margin(*args):
    return sum(args)
a = calculate_margin(2,3,4,5,6)
print(a)

def total_expenses(rent, phone_bill):
    return rent + phone_bill
total_expenses = total_expenses(900,800)
print(total_expenses)
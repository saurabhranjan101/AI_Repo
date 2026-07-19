## Exercise: The Chai Bill Calculator
'''
You run a chai stall. Customers order multiple cups of chai, sometimes with add-ons (extra ginger, masala, biscuits). Write a function to calculate their bill.
Your task:
Write a function chai_bill(cups, *addons, **discount) that:

Charges ₹15 per cup of chai
Adds ₹5 for each addon passed via *args (like "ginger", "masala", "biscuit")
Applies a discount only if discount_percent is passed via **kwargs
Returns the final bill amount

Test it with these calls:

print(chai_bill(2))                                              
print(chai_bill(3, "ginger", "masala"))                          
print(chai_bill(4, "biscuit", discount_percent=10))              
print(chai_bill(5, "ginger", "masala", "biscuit", discount_percent=20))

Expected output:

* 30
* 55
* 58.5
* 112.0
'''

def chai_bill(cups, addons_count=0, **discount):
    total = cups * 15
    total += addons_count * 5
    if "discount_percent" in discount:
        total -= (discount["discount_percent"] / 100) * total
    return total
cups = int(input("How many cups of tea?"))
addon = int(input("How many addons you want - 1/2/3 ? "))
discount_percent = 10
Bill = chai_bill(cups, addons_count=addon, discount_percent=10)
print(f"Youer chai bill is {Bill}")
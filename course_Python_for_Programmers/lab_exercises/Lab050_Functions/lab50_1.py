#!/usr/bin/env python3
"""lab50_1.py
CalculateCost function returns a total cost from the sales price and sales tax rate.
Default value for the tax rate = 8.25%.
"""


def CalculateCost(price, rate=8.25):
    tax = price * (rate / 100)
    return f"Total cost: ${price+tax:.2f}"


print(CalculateCost(10.50))
print(CalculateCost(10.50, 3.5))

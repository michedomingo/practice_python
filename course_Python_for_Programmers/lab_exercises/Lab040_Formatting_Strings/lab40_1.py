#!/usr/bin/env python3
"""lab40_1.py
Requests a floating point number from user, asks for the number
of digits to the right of the decimal, and presents result of squaring the number
formatted with number of digits to the right of the decimal.
"""
while True:
    num_to_square = input("Number to square please: ")
    try:
        num = float(num_to_square)
    except ValueError:
        print("Please try again.")
    else:
        break

while True:
    try:
        dec_digits = int(input(
            "How many digits to the right of the decimal place would\nyou like to have displayed? "))
    except ValueError:
        print("Please try again.")
    else:
        break

print(f"{num} squared is {num**2:.{dec_digits}f}.")

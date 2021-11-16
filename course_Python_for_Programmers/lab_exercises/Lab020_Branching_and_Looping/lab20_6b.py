#!/usr/bin/env python3
"""lab20_6b.py
Prints the decimal equivalent of a binary string.
Test with binary string: "1011". Decimal equivalent: 11
int builtin is useful or use a for or while loop.
>>> help(int)
"""
binary_string = '1011'
sum = 0

for index, char in enumerate(reversed(binary_string)):
    if char not in '01':
        print(f"{binary_string} is not a binary string.")
        break
    else:
        digit = int(char) * (2 ** index)
        sum += digit
        if index == (len(binary_string) - 1):
            print(
                f"The binary string '{binary_string}' decimal equivalent is {sum}.")

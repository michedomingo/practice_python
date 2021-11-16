#!/usr/bin/env python3
"""lab20_6.py
Prints the decimal equivalent of a binary string.
Test with binary string: "1011". Decimal equivalent: 11
"""


def ConvertBinaryToDecimal(binary):
    for char in binary:
        if char not in '01':
            print(f"{binary} is not a binary string.")
            break
    else:
        decimal = 0
        for position_weight in range(len(binary)):
            digit = GetReversedBinaryDigit(binary, position_weight)
            decimal += digit * (2 ** position_weight)
        print(
            f"The binary string '{binary}' decimal equivalent is {decimal}.")


def GetReversedBinaryDigit(binary, position_weight):
    string_reversed = binary[::-1]
    digit = int(string_reversed[position_weight])
    return digit


def main():
    ConvertBinaryToDecimal("1011")


main()

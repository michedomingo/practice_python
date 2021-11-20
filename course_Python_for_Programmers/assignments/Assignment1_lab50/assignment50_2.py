#!/usr/bin/env python3
"""assignment50_2.py
FahrenheitToCentigrade function takes in temperature in Fahrenheit, returns in Centigrade.
CentigradeToFahrenheit function takes in temperature in Centigrade, returns in Fahrenheit.
ShowConversion function prints two charts using the conversion functions.
VerifyConversion function confirms big range of fahrenheit values is not different after converting.
"""


def FahrenheitToCentigrade(f):
    return round((f - 32) * 5/9)


def CentigradeToFahrenheit(c):
    return round(9/5 * c + 32)


def ShowConversion():
    print("  C ->     F")
    for centigrade in range(0, 101, 10):
        print(f"{centigrade:>3} ->   {CentigradeToFahrenheit(centigrade):>3}")
    print("----\n\n  F ->     C")
    for fahrenheit in range(0, 221, 10):
        print(f"{fahrenheit:>3} ->   {FahrenheitToCentigrade(fahrenheit):>3}")


def VerifyConversion():
    for f in range(0, 221, 10):
        c = FahrenheitToCentigrade(f)
        f2 = CentigradeToFahrenheit(c)
        if abs(f2 - f) > 1:
            print("fix error")


def main():
    ShowConversion()
    VerifyConversion()


main()

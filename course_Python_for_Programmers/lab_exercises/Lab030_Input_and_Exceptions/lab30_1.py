#!/usr/bin/env python3
"""
1. Write a program that asks the user name, 
then asks for the amount of money and to give you half.
There is nothing to check about the name given.
"""

name = input("Name please: ")

while True:
    try:
        money = float(input("How much money do you have? "))
        break
    except ValueError:
        print("Please try again.")

print(f"{name}, give me ${money/2:,.2f}.")

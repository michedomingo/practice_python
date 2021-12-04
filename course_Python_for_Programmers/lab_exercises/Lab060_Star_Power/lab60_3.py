#!/usr/bin/env python3
"""lab60_3.py
3. Make a MakePizza() function. It takes in any number of arguments. The first two are
the main ingredients and are required.
"""


def MakePizza(i1, i2, *rest):
    print(f"Here’s your {i1} and {i2} pizza, with ", end='')
    for ingredient in rest:
        print(ingredient, end=" ")
    print("\nEnjoy!")


def main():
    ingredients = "anchovies", "garlic", "oregano", "tomato", "peppers"
    MakePizza(*ingredients)
    MakePizza("cheese", *ingredients)


main()

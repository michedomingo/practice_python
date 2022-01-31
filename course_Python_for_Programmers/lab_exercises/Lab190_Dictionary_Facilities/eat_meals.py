#! /usr/bin/env python3
"""
import into lab190.py to test CallThis function
"""


def DoBreakfast(meat="bacon", eggs="scrambled"):
    return f"Have some {meat} and {eggs} eggs.  Enjoy!"


def DoLunch(**substitutions):
    menu = {"meat": "ham", "cheese": "american", "bread": "white"}
    menu.update(substitutions)
    return "Here's your %(meat)s and %(cheese)s on %(bread)s bread." % (menu)


def DoTea():
    return "Tea time!"


def DoDinner(menu):
    return f"{menu.title()} for dinner tonight."


def main():
    print(DoBreakfast("sausage", eggs="scrambled"))
    print(DoLunch(cheese="swiss", bread="rye"))
    print(DoTea())
    print(DoDinner("roast beef"))


if __name__ == "__main__":
    main()
"""
$ eat_meals.py
Have some sausage and scrambled eggs.  Enjoy!
Here's your ham and swiss on rye bread.
Tea time!
Roast Beef for dinner tonight.
$ 
"""

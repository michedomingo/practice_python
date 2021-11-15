#!/usr/bin/env python3
"""lab50_2.py
DoBreakfast function takes 5 arguments: meat, eggs, potatos, toast, and beverage. 
Call it at least 3 different times with different orders.
"""


def DoBreakfast(meat='bacon', eggs='over easy', potatoes='hash browns', toast='white', beverage='coffee'):
    print(f"Here is your {meat} and {eggs} eggs with {potatoes} and {toast} toast.",
          f"Can I bring you more {beverage}?", sep='\n')


def main():
    DoBreakfast()
    DoBreakfast("ham", "basted", "cottage cheese",
                "cinnamon", "orange juice")
    DoBreakfast("sausage", beverage="chai", toast="wheat")


main()

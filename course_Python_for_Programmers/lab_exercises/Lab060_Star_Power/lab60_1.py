#!/usr/bin/env python3
"""lab60_1.py
DoBreakfast function takes 5 arguments: meat, eggs, potatos, toast, and beverage. 
Update from lab50_2.py: Unpack 'favorites' sequence into the function call with * (star/asterisk)
"""


def DoBreakfast(meat='bacon', eggs='over easy', potatoes='hash browns', toast='white', beverage='coffee'):
    print(f"Here is your {meat} and {eggs} eggs with {potatoes} and {toast} toast.",
          f"Can I bring you more {beverage}?", sep='\n')


def main():
    favorites = ("ham", "poached", "home fried", "English muffin")
    DoBreakfast()
    DoBreakfast(*favorites)


main()

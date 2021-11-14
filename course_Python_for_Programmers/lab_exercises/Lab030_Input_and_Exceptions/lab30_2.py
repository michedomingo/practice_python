#!/usr/bin/env python3
"""
2. (Optional) Write a program that asks the user to think of a number between 1 and 10.
The program then tries to guess the number and asks the user if the computer’s guess
is right. If the guess is not right, ask the user if the guess is high or low and then take
another guess. When the guess is correct, report how many guesses it took to get the
right number.
"""
count = 0
num = 5

print("Think of a number between 1 and 10 and I'll try to count it.")
while True:
    answer = input(f"""Is your number {num}?\nPlease press:
        'y' for yes
        'n' for no
        """)
    if answer == 'y':
        count += 1
        break
    elif answer == 'n':
        while True:
            count += 1
            guess = input(f"""No? Then please press:
            'h' if {num} is higher than your number
            'l' if {num} is lower than your number
            """)
            if guess == 'h':
                num -= 1
                break
            elif guess == 'l':
                num += 1
                break
            else:
                count -= 1
                print("Please try again.", end=' ')
    else:
        print("Please try again.", end=' ')

print(f"Hurray! Only {count} guess(es).")

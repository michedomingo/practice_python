#!/usr/bin/env python3
"""lab120_2a.py
2. Make another program module (lab120_2.py) in the same directory as your lab120_1.py.
Ask the user for some input and then report the number of vowels in the input. 
It will import lab120_1.py to do the vowel counting.
"""
import lab120_1a


def InputVowelCount():
    user_input = input("Type a sentence: ")
    print(lab120_1a.CountVowels(user_input))


if __name__ == "__main__":
    InputVowelCount()

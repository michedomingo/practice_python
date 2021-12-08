#!/usr/bin/env python3
"""lab120_1a.py
1. Write a function that returns the number of vowels in the string.
Be sure that your test does not run when your module is imported.
In the interpreter, import your module and run help on your module and fix up the documentation.
"""


def CountVowels(words):
    """
    When passed a string of characters, returns the number of vowels in the string.
    Vowels are ’a’, ’e’, ’i’, ’o’, ’u’.
    """
    count = 0
    for word in words:
        for char in word.lower():
            if char in "aeiou":
                count += 1
    return count


def TestCountVowels():
    """Tests CountVowels() function with the sentence:
    “Math, science, history, unraveling the mysteries, that all started with the big bang!”. 
    It has 22 vowels.
    """
    words = ["Math, science, history, ", "unraveling the mysteries, ",
             "that all started with the big bang!"]
    print("The sentence:")
    for word in words:
        print(word, end="")
    print(f"\n...has {CountVowels(words)} vowels.")


if __name__ == "__main__":
    TestCountVowels()

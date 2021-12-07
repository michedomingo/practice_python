#!/usr/bin/env python3
"""lab110_1b.py
1. Write a function that collects words from the user until the user does not give one.
(Use a list for this. We’ll learn about sets later.) If the word given was given before,
capitalized or not, report that. When the user stops giving words, return a single string
that has all the words given, once each, all upper-case, in alphabetical order, with "
AND " between them, and ’!!!’ at the end.
"""


def CollectWords():
    """Collects words into a sentance.
    """
    words = []
    while True:
        new_word = input("Word please: ")
        if not new_word:
            break
        upped_word = new_word.upper()
        if upped_word in words:
            print(f"{new_word} is already given.")
        else:
            words.append(upped_word)
    words.sort()
    return ' AND '.join(words) + '!!!'


def main():
    print(CollectWords())


main()

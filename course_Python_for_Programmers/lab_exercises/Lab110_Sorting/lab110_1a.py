#!/usr/bin/env python3
"""lab110_1a.py
1. Write a function that collects words from the user until the user does not give one.
(Use a list for this. We’ll learn about sets later.) If the word given was given before,
capitalized or not, report that. When the user stops giving words, return a single string
that has all the words given, once each, all upper-case, in alphabetical order, with "
AND " between them, and ’!!!’ at the end.
"""


def CollectWords():
    words, output = [], ""
    while True:
        user_input = input("Word please: ")
        uppercase_word = user_input.upper()
        if uppercase_word in words:
            print(f"{user_input} is already given.")
        elif not user_input:
            break
        else:
            words.append(uppercase_word)
    words.sort()
    last_word = words[-1]

    for word in words[:-1]:
        output += f"{word} AND "

    return f"{output}{last_word}!!!"


def main():
    print(CollectWords())


main()

#!/usr/bin/env python3
"""assignment120_1.py
Confirms whether a given word is is a valid
Python identifier to use in your Python programs.
"""
import keyword


def IsValidIdentifier(word):
    """
    Receives a string and returns a tuple 
    (True_or_False, reason_string) dependent on
    the candidate identifier following the rules:
    (a) The first character must be a letter or underscore.
    (b) Letters beyond the first can be alphanumeric or underscore.
    (c) Identifiers can not be keywords.
    """
    if word[0].isdigit():
        return False, f"{word} -> Invalid: first symbol must be alphabetic or underscore."

    elif not word.isalnum():
        for char in word:
            if char == '_':
                continue
            elif not char.isalnum():
                return False, f"{word} -> Invalid: ’{char}’ is not allowed."

    elif word in keyword.kwlist:
        return False, f"{word} -> Invalid: this is a keyword!"

    return True, f"{word} -> Valid!"


def main():
    """
    Tests the IsValidIdentifier function with candidate identifiers.
    Note: testing only happens when this module is the __main__ module.
    """
    DATA = ["and", "*star", "x", "_x", "2x",
            "x,y", "yield", "is_this_good", "x y"]
    for test in DATA:
        print(IsValidIdentifier(test))


if __name__ == "__main__":
    main()

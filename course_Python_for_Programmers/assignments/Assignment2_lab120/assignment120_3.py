#!/usr/bin/env python3
"""assignment120_3.py
Program that imports assignment120_1 and 
uses assignment120_1.IsValidIdentifier() 
to test identifiers collected from user input.
"""
import assignment120_1


def main():
    while True:
        test_identifiers = input("Test valid Python identifiers: ")
        if not test_identifiers:
            break
        print(assignment120_1.IsValidIdentifier(test_identifiers))


if __name__ == "__main__":
    main()

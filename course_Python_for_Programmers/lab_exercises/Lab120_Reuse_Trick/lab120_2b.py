#!/usr/bin/env python3
"""lab120_2a.py
Interactive vowel counter.
"""

import lab120_1b


def main():
    while True:
        count_this = input("Phrase: ")
        if not count_this:
            break
        print(f"... has {lab120_1b.CountVowels(count_this)} vowels.")


if __name__ == "__main__":
    main()

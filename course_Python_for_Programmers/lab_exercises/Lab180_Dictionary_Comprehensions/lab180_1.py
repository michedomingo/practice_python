#!/usr/bin/env python3
"""lab180_1.py
Make a dictionary of the words: Keep a fire burning in your eye.
key: lower-case version of the word
value: will be the word backwords
"""


def ReverseDict(text):
    return {k.lower(): k.lower()[::-1] for k in text.split()}


def main():
    word_dict = ReverseDict("Keep a fire burning in your eye.")
    print(word_dict)
    print('\n'.join(f"{k:>10}:{word_dict[k]}" for k in sorted(word_dict)))


if __name__ == "__main__":
    main()

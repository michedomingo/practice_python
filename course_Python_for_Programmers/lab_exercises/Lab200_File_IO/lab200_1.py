#!/usr/bin/env python3
"""lab200_1.py
Takes a file name, returns number of vowels in file's text
"""
import sys
import lab150_2 as count_vowels


def CountVowelsInFile(file_name):
    vowel_count = 0
    with open(file_name) as file_obj:
        for line in file_obj:
            vowel_count += count_vowels.CountVowels(line)
    return vowel_count


def main():
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = input("File name: ")
    if not file_name:
        file_name = "cats.txt"
    try:
        print(
            f"There are {CountVowelsInFile(file_name)} vowels in {file_name}.")
    except IOError as info:
        print(info, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

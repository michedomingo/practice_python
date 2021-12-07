#!/usr/bin/env python3
"""lab110_2a.py
2. You have a list of strings representing names:
["Jack Sparrow", "George Washington", "Tiny Sparrow", "Jean Ann Kennedy"]
Sort them by last name and print them, last name first. 
"""


def SortNames(names):
    last_first_names = []
    for name in names:
        split_name = name.rsplit(None, 1)
        last_first_names.append(', '.join(reversed(split_name)))

    last_first_names.sort()
    return '\n'.join(last_first_names)


def main():
    names = ["Jack Sparrow", "George Washington",
             "Tiny Sparrow", "Jean Ann Kennedy"]
    print(SortNames(names))


main()

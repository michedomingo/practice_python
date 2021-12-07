#!/usr/bin/env python3
"""lab110_2b.py
2. You have a list of strings representing names:
["Jack Sparrow", "George Washington", "Tiny Sparrow", "Jean Ann Kennedy"]
Sort them by last name and print them, last name first. 
"""


def ReverseName(name):
    """Returns the "last_name, first_names" version
    of the name.
    """
    parts = name.split()
    return parts[-1] + ', ' + ' '.join(parts[:-1])


def ReverseName(name):
    parts = name.split()
    return parts.pop() + ', ' + ' '.join(parts)


def ReverseName(name):
    parts = name.rsplit(None, 1)
    return parts[-1] + ', ' + parts[0]


def ReverseName(name):
    *first_names, last_name = name.split()
    return last_name + ', ' + ' '.join(first_names)


def main():
    NAMES = ["Jack Sparrow", "George Washington",
             "Tiny Sparrow", "Jean Ann Kennedy"]

    def ReverseThem():
        for name in sorted(NAMES, key=ReverseName):
            print(ReverseName(name))

    def ReverseThem():
        reversed_names = []
        for name in NAMES:
            reversed_names += [ReverseName(name)]
        for name in sorted(reversed_names):
            print(name)
    ReverseThem()


main()

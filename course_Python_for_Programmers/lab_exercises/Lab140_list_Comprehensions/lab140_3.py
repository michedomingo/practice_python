#!/usr/bin/env python3
"""lab140_3.py
3. Provide a MakeString function that receives a glue string, and any number of words
and returns a string containing all of the words, each separated by the glue string.
"""


def MakeString(glue, *objects):
    return glue.join([str(obj) for obj in objects])


def main():
    print(MakeString("*", "this", "that", "other"))
    print(MakeString("_", "you", "are", "awesome", "#1", 100))
    print(MakeString(", ", *range(10, 0, -1)))
    print(MakeString('*', '1', 2, "word"))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""assignment50_1b.py
PrintSentence function receives a noun and a verb as arguments.
Prints "All of our <the noun> wanted to <the verb>."
"""


def PrintSentence(noun, verb):
    print(f"All of our {noun} wanted to {verb}.")


def main():
    PrintSentence("plants", "grow")
    PrintSentence("friends", "dance")
    PrintSentence("family", "eat")


main()

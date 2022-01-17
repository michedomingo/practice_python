#!/usr/bin/env python3
"""lab140_4.py
4. Use list comprehension to make a function that returns a list of strings, each string
emulating one card, and the whole list emulating a deck of cards. In your caller, print
out the cards, comma-separated, except stick in "and" before the last card.
"""


def MakeCards():
    values = [num for num in range(
        2, 11)] + ["Jack", "Queen", "King", "Ace"]
    # print(f"\n\tvalues: {values}")
    suites = ["Clubs (♣)", "Diamonds (♦)", "Hearts (♥)", "Spades (♠)"]
    # print(f"\tsuite: {suites}\n")
    deck = [
        f"{value} of {suite}" for value in values for suite in suites] + ["Joker"] * 2
    # print(f"deck before main:\n{deck}\n")
    return deck


def main():
    deck = MakeCards()
    print(f"{', '.join(deck[:-1])}, and {deck[-1]}")


if __name__ == "__main__":
    main()

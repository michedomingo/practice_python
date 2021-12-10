#!/usr/bin/env python3
"""lab140_4.py
4. Use list comprehension to make a function that returns a list of strings, each string
emulating one card, and the whole list emulating a deck of cards. In your caller, print
out the cards, comma-separated, except stick in "and" before the last card.
"""


def MakeCards():
    values = [num for num in range(
        2, 11)] + ["Jack", "Queen", "King", "Ace"]
    suites = ["Clubs (♣)", "Diamonds (♦)", "Hearts (♥)", "Spades (♠)"]
    deck = [
        f"{value} of {suite}" for value in values for suite in suites] + ["Joker"] * 2
    return deck


def main():
    deck = MakeCards()
    print(f"{', '.join(deck[:-1])}, and {deck[-1]}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""lab80_1.py
1. Write a function called FlipCoin that emulates the flip of a coin, returning "heads" or
"tails". Find a way to test it.
"""
import random


def FlipCoin():
    # side = random.randint(1, 2)
    # if side == 1:
    #     return "heads"
    # return "tails"
    if random.randrange(0, 2) == 0:
        return "heads"
    return "tails"


def main(num_times):
    """Driver for testing."""
    # print(f"Testing FlipCoin function returns: {FlipCoin()}")
    heads = 0
    for n in range(num_times):
        if FlipCoin() == "heads":
            heads += 1
    print(f'With {num_times} flips, "heads" came up {heads} '
          f"times, or {heads/num_times:.1%} of the flips.")


main(100)

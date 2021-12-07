#!/usr/bin/env python3
"""lab80_3b.py
3. Modify lab80_1.py by adding a function called GetHeads(target) that uses FlipCoin().
This new function accepts an integer as the only argument, target, and
then flips coins until it gets target heads in a row.
It returns the number of flips it took to get target heads in a row.

Write another function that calls GetHeads(target) over and over, number_of_experiments
times where number_of_experiments is given as an argument, as is target. Have this
new function calculate the average result and print a report.
"""

import random


def FlipCoin():
    """Simulates the flip of a coin."""

    if random.randrange(0, 2) == 0:
        return "tails"
    return "heads"


def GetHeads(target):
    """Flips coins until it gets target heads in a row."""

    heads = count = 0
    while heads < target:
        count += 1
        if FlipCoin() == "heads":
            heads += 1
        else:          # "tails"
            heads = 0
    return count


def GetAverage(number_of_experiments, target):
    """Calls GetHeads(target) that number_of_experiments
    times and reports the average."""

    total = 0
    for n in range(number_of_experiments):
        total += GetHeads(target)
    print(f"Averaging {number_of_experiments} experiments, it took {total/number_of_experiments:.1f} coin flips to get {target} in a row.")


GetAverage(100, 3)

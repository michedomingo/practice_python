#!/usr/bin/env python3
"""lab80_3.py
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
    if random.randrange(0, 2) == 0:
        return "heads"
    return "tails"


def GetHeads(target):
    count, tails, result = 0, 0, []
    while True:
        count += 1
        result.append(FlipCoin())
        if ('tails' in result):
            tails += 1
            result = []
        elif len(result) == target:
            heads = count - tails
            return count, heads
            break


def CalculateAverageResult(number_of_experiments):
    total_count = 0
    total_heads = 0

    for num in range(number_of_experiments):
        count, heads = GetHeads(number_of_experiments)
        total_count += count
        total_heads += heads

    print(f'''With {total_count} flips from {number_of_experiments} experiments,
        "heads" came up {total_heads} times, or {total_heads/total_count:.1%} of the flips.''')


def main():
    CalculateAverageResult(2)


main()

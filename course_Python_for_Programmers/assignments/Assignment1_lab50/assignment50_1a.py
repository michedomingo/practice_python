#!/usr/bin/env python3
"""assignment50_1a.py
JudgeNumber function receives a number & returns it formatted to one decimal place.
Input: print(JudgeNumber(32))
Output: "Good number 32.0."
"""


def JudgeNumber(num):
    return f"Good number {float(num):.1f}."


def main():
    print(JudgeNumber(32))
    print(JudgeNumber(1.4))
    print(JudgeNumber("1"))


main()

#!/usr/bin/env python3
"""lab100_3a.py
3. Write a function that takes in any number of colors. 
It finds the first two primary colors given and returns the result of mixing them together. 
If there are not two primary colors, the result should be "grey".
Primary colors are: red, yellow and blue.
"""


def MixColors(*colors):
    primary_colors = 'red', 'yellow', 'blue'
    two_colors = []
    color_count = 0

    for color in colors:
        if color in primary_colors:
            two_colors.append(color)
            color_count += 1
        if color_count == 2:
            break
    else:
        print(f"Colors {colors} results in - grey\n")

    if two_colors[0] == two_colors[1]:
        print(
            f"{colors} colors, 1st two primary colors {two_colors} results in - {two_colors}\n")

    if "red" in two_colors:
        if "blue" in two_colors:
            print(
                f"{colors} colors, 1st two primary colors {two_colors} results in - purple\n")
        if "yellow" in two_colors:
            print(
                f"{colors} colors, 1st two primary colors {two_colors} results in - orange\n")
    if "yellow" in two_colors:
        if "blue" in two_colors:
            print(
                f"{colors} colors, 1st two primary colors {two_colors} results in - green\n")


def main():
    MixColors('red', 'blue', 'purple')
    MixColors('blue', 'red', 'purple')
    MixColors('red', 'purple', 'pink')
    MixColors('blue', 'purple', 'yellow')
    MixColors('purple', 'pink', 'blue')
    MixColors('yellow', 'red', 'blue')


main()

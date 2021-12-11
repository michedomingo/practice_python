#!/usr/bin/env python3
"""lab150_1.py
1. Write a function that uses enumerate to display colors
sorted and formatted four across columns.
"""


def PrintColors(colors):
    for index, color in enumerate(sorted(colors)):
        # print(index, color)
        print(f"{color:>15}", end=" ")
        if index % 4 == 3:
            print()


def main():
    colors = ["beige", "silver", "charcoal", "royal blue", "aquamarine", "forest green",
              "chartreuse", "lime", "golden", "goldenrod", "coral", "salmon", "hot pink",
              "fuchsia", "lavender", "plum", "indigo", "maroon", "crimson", "lemon"]
    PrintColors(colors)


if __name__ == "__main__":
    main()

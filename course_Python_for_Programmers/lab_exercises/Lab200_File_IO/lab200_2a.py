#!/usr/bin/env python3
"""lab200_2a.py
Copies cat.txt into area, changes text in file
replacing word_1 with word_2 & vice-versa
"""
import do_swap
import shutil


def Swapper(file_name, word_1, word_2):
    try:
        with open(file_name, "r+") as open_file:
            text = open_file.read()
            text = do_swap.DoSwap(text, word_1, word_2)
            open_file.seek(0, 0)
            open_file.truncate()
            open_file.write(text)
    except OSError as info:
        print(f"Can't open {file_name} because {info}")


def main():
    shutil.copy("cats.txt", "cats2.txt")
    Swapper("cats2.txt", "cat", "dog")
    Swapper("www.txt", "www", "yyy")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""lab200_2b.py (updated from lab200_2a)
Copies cat.txt into area, changes text in file
replacing word_1 with word_2 & vice-versa
Use builtin file iterator so file not in memory at one time & use tempfile
"""
import os
import shutil
import tempfile
import do_swap


def Swapper(file_name, word_1, word_2):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        # temp_file is an open file object, open for writing
        try:
            with open(file_name) as open_file:
                for line in open_file:
                    swapped_line = do_swap.DoSwap(line, word_1, word_2)
                    temp_file.write(bytes(swapped_line,
                                          encoding="utf-8"))
        except OSError as info:
            print(f"Problem with {file_name} because {info}")

    # For Windows, first: os.remove(file_name)
    os.rename(temp_file.name, file_name)


def main():
    shutil.copy("cats.txt", "cats2.txt")
    Swapper("cats2.txt", "cat", "dog")
    Swapper("www.txt", "www", "yyy")


if __name__ == "__main__":
    main()

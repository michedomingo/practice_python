#!/usr/bin/env python3
"""
Faulty DoSwap function for importing to lab200_2.py
for swapping occurrences of "word_2" for "word_1" & occurrences of "word_1" for "word_2" in the text.
Faulty for this exercise bc case-sensitive & it would change "category" to "dogegory".
"""


def DoSwap(text, word_1, word_2):
    """
    Returns swapped text
    """

    dummy = "make_space"
    while True:
        if text.find(dummy) == -1:
            break
        dummy *= 2
    text = text.replace(word_1, dummy)
    text = text.replace(word_2, word_1)
    text = text.replace(dummy, word_2)
    return text


if __name__ == "__main__":
    print(
        DoSwap("""Some dogs and cats played together. [make_space]""", "dog", "cat"))

"""        
$ do_swap.py
Some cats and dogs played together.
$ 
"""

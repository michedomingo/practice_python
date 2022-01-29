#!/usr/bin/env python3
"""lab150_2.py
2. Update lab120_1.py with enumerate function to count ’y’s as vowels by specs.
Count a ’y’ as a consonant (non vowel):
• if it is the first character.
• if it is preceded by a vowel: boy, way, hey.
Count a ’y’ as a vowel:
• if the word ends with ying: flying, spying.
• if it is at the end of a word, and is preceded by a consonant: fly.
• if it preceded and followed by a consonant: myth, satyr.
"""
import string


def CountVowels(phrase):
    """
    When passed a string of characters, returns the number of vowels in the string.
    Vowels are ’a’, ’e’, ’i’, ’o’, ’u’.
    Updated to include 'y' counts based on specs above.
    """
    REAL_VOWELS = "aeiou"
    chars_to_strip = string.punctuation + "0123456789_"
    count = 0

    for word in phrase.lower().split():
        word = word.strip(chars_to_strip)
        word_length = len(word)
        # return word, word_length
        for index, char in enumerate(word):
            if char in REAL_VOWELS:
                count += 1
                continue
            if char != 'y' or index == 0:
                # char is 'y' & is not the first char
                continue
            if word.endswith("ying") and index == word_length - 4:
                count += 1
                continue
            if (index == word_length - 1 or word[index+1] not in REAL_VOWELS):
                # 'y' preceded by a consonant at end of word or followed by a consonant
                count += 1
                continue
    return count


def main():
    """Tests the CountVowels function"""
    for test in (
        """Math, science, history, unraveling the mysteries,
        that all started with the big bang!""",
            "boy way hey myth satyr fly flying spying",):
        # print(CountVowels(test), test)
        print(CountVowels(test), test)


if __name__ == "__main__":
    main()

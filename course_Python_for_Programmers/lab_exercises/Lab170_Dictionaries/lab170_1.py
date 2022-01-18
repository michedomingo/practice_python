#!/usr/bin/env python3
"""lab170_1.py
Dictionary implementation for demonstrating a Python dictionary.
"""


def SetUpPyDict():
    py_dict1 = {}

    py_dict2 = {"break": "break from a loop and skip the else",
                "continue": "go to the next iteration of the loop",
                "for": "set up looping"}

    # Updating py_dict1 with py_dict2's keys and values.
    # If py_dict2 has keys already in py_dict1, py_dict2's
    # values will replace the old values for the key.
    py_dict1.update(py_dict2)
    # If you add an entry with a duplicate key, the new
    # meaning will be the one that sticks:
    py_dict1["pass"] = "do nothing"

    return py_dict1


def CollectEntries(py_dict):
    """Collects new entries for the dictionary"""
    while True:
        word = input("Word: ")
        if not word:
            return
        meaning = input("Meaning: ")
        py_dict[word] = meaning


def PrintDefinitions(py_dict):
    """Prints the dictionary alphabetically by meaning"""
    # for meaning in sorted(py_dict.values()):
    #     print(f"{meaning} : {py_dict[meaning]}")
    for word in sorted(py_dict):
        print(f"{py_dict.get(word)} : {word}")


def FindDefinitions(py_dict):
    """Reports a key:value pair for a given key"""
    while True:
        word = input("Word to find: ")
        if not word:
            return
        try:
            print(f"{word} : {py_dict[word]}")
        except KeyError:
            print(f"{word} is not in the dictionary.")


def MakePrompt(choices):
    choice_list = sorted(choices)
    guts = ", ".join([f"({choice[0]}){choice[1:]}"
                      for choice in choice_list])
    return f"Choose {guts} (enter to quit) "


def PrintEntries(py_dict):
    """Prints out the dictionary entries, sorted by key"""
    for word in sorted(py_dict):
        print(f"{word} : {py_dict[word]}")


def RunMenu(py_dict):
    """Runs the user interface for dictionary manipulation"""
    # The choices dictionary has function names for values.
    choices = {"add": CollectEntries, "definitions": PrintDefinitions, "find": FindDefinitions,
               "print": PrintEntries}
    prompt = MakePrompt(choices)

    while True:
        raw_choice = input(prompt)
        if not raw_choice:
            break
        given_choice = raw_choice[0].lower()
        for maybe_choice in choices:
            if maybe_choice[0] == given_choice:
                # The appropriate function is called using the
                # dictionary value for the name of the function.
                choices[maybe_choice](py_dict)
                break
        else:
            print(f"{raw_choice} is not an acceptible choice.")


def main():
    py_dict = SetUpPyDict()
    RunMenu(py_dict)


if __name__ == "__main__":
    main()

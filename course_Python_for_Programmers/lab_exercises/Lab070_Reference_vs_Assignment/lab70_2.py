#!/usr/bin/env python3
"""lab70_2.py
2. Define a function that will produce an error because the interpreter doesn’t knowwhich
pi you want.

Output:
Traceback (most recent call last):
  File "lab70_2.py", line 36, in <module>
    main()
  File "lab70_2.py", line 33, in main
    Crash()
  File "lab70_2.py", line 23, in Crash
    pi += "orange"
UnboundLocalError: local variable 'pi' referenced before assignment
"""
pi = 3.14


def Report(message):
    print(f"{message} pi = {pi}.")


def SetLocal():
    pi = "yellow"


def SetGlobal():
    global pi
    pi = "red"


def Crash():
    pi += "orange"


def main():
    Report("Starting:")
    SetLocal()
    Report("After SetLocal():")
    SetGlobal()
    Report("After SetGlobal():")
    Report("\nBefore Crash():")
    Crash()


main()

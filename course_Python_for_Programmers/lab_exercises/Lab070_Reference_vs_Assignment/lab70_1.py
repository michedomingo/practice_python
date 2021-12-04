#!/usr/bin/env python3
"""lab70_1.py
1. Predict the output.

Output:
 Starting : pi = 3.14.
 After Set ():  pi = 3.14.
 After SetGlobal ():  pi = red .
"""
pi = 3.14


def Report(message):
    print(f"{ message } pi = {pi }.")


def SetLocal():
    pi = " yellow "


def SetGlobal():
    global pi
    pi = "red "


def main():
    Report(" Starting :")
    SetLocal()
    Report(" After Set (): ")
    SetGlobal()
    Report(" After SetGlobal (): ")


main()

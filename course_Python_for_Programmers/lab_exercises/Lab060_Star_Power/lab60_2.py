#!/usr/bin/env python3
"""lab60_2.py
2. You have: tools = "hammer", "wrench", "scissors", "pliers", "ruler"
(a) How would you isolate "scissors" into the identifier to_cut and put the rest
into meaningless identifiers, as few as possible?
(b) What would rest will result?
to_hit, to_torque, to_cut, to_pinch, to_measure, *rest = tools
"""


def PrintIdentifiers():
    tools = "hammer", "wrench", "scissors", "pliers", "ruler"

    *rest, to_cut, to_pinch, to_measure = tools
    print(f"""(a) *rest, to_cut, to_pinch, to_measure = tools
    tools = {tools}
    *rest = {[*rest]},
    to_cut = {to_cut},
    to_pinch = {to_pinch},
    to_measure = {to_measure}""")

    to_hit, to_torque, to_cut, to_pinch, to_measure, *rest = tools
    print(f"""(b) to_hit, to_torque, to_cut, to_pinch, to_measure, *rest = tools
    tools = {tools}
    to_hit = {to_hit}
    to_torque = {to_torque},
    to_cut = {to_cut},
    to_pinch = {to_pinch},
    to_measure = {to_measure},
    *rest = {[*rest]}""")


def main():
    PrintIdentifiers()


main()

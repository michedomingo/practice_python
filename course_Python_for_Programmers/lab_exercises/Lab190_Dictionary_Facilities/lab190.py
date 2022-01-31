#!/usr/bin/env python3
"""lab190.py
Update from lab50_2.py
CallThis() requires one positional argument function identifier
& any number of any kind of arguments, reports function named,
arguments given, & returned value(s)
"""
import eat_meals


def CallThis(function_object, *tuple_args, **keyword_args):
    """calls a function passing unknown arguments"""
    # print()
    report = f"{function_object.__name__}("
    # print(f"\ttuple_args: {tuple_args}     keyword_args: {keyword_args}\n")
    all_args = [str(t) for t in tuple_args] + [
        "%s=%s" % (k, v) for k, v in keyword_args.items()]
    # print(f"\tall_args: {all_args}\n")
    result = function_object(*tuple_args, **keyword_args)
    report += f"{', '.join(all_args)})  -->  {result}"
    # print(f"\nREPORT: {report}\n")
    print(report)
    return result


def main():
    print(CallThis(eat_meals.DoBreakfast))
    print(CallThis(eat_meals.DoBreakfast, "ham", eggs="basted"))
    # print(CallThis(eat_meals.DoLunch, cheese="gouda", bread="wheat"))
    # print(CallThis(eat_meals.DoTea))
    # print(CallThis(eat_meals.DoDinner, "stew"))


main()

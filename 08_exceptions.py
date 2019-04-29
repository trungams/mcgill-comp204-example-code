#!/usr/bin/env python3

"""This file contains example code for exception handling in Python
"""


class ExceptionName(Exception):
    pass


class SimpleException(Exception):
    pass


def risky_computation_that_might_result_in_division_by_zero():
    pass


try:
    risky_computation_that_might_result_in_division_by_zero()
    pass
except ExceptionName:
    print("ExceptionName happened, mission abort")
except SimpleException:
    print("just a simple exception, starting over...")
    pass
else:
    print("if no exception is raised by the operation in try block, print this message")
finally:
    print("this ALWAYS execute right after the try")

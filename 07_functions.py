#!/usr/bin/env python3

"""This file contains example code for function in Python
"""

import math


def add_two_numbers(x, y):
    """This function returns the sum of 2 integers"""
    if not (isinstance(x, int) and isinstance(y, int)):
        return None
    else:
        return x + y


# This function performs primality testing on the number n
def is_prime(n):
    """Returns True if n is a prime number, False otherwise"""

    if n <= 1:
        return False    # 0 and 1 are prime numbers
    if n == 2:
        return True     # 2 is a prime number
    if n % 2 == 0:
        return False    # even numbers greater than 2 are not prime
    # For every integer 1 < i < n, if n is divisible by i,
    # then n is not prime. We only need to check from 3 to
    # sqrt(n), because sqrt(n) is the second largest factor of n,
    # and we can increase i by 2 at every iteration, since we know
    # that n is not even
    limit = math.floor( math.sqrt(n) ) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


def change_value(x : int):
    """What does this function do?"""

    # x is now its square, but the value of the original variable 
    # in the calling function does not change
    x *= 2


def change_list(lst: list):
    """What does this function do?"""

    # the first element of the list is replaced by its square
    lst[0] *= lst[0]


def get_tuple():
    x = 1
    y = "i'm a message"
    z = [0 for _ in range(3)]
    return x, y, z


if __name__ == '__main__':

    # pass by value
    x = 10
    print(x)
    change_value(x)
    print(x)

    # pass by reference
    lst = [10, 9, 8, 7]
    print(lst)
    change_list(lst)
    print(lst)

    # we can 'unpack' the return value of a function
    a,b,c = get_tuple()
    print(get_tuple())
    print(a, b, c)


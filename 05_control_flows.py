#!/usr/bin/env python3

"""This file contains example code for control flows in Python,
namely conditionals, for loops, while loops
"""

import math


# Since a Python script can be either run as a single program
# or imported as a module, in both cases, the Python interpreter
# will go from top to bottom and execute any instruction it
# encounters. However, sometimes we only want to run a block of
# code if and only if our script is run as the main program.
# The condition below helps us achieve that
if __name__ == '__main__':

    # Working with if-else statements
    print("This message is always displayed when the program is run")
    if True:
        print("But should the program print this message?")
    elif True:
        print("My condition always hold true, so this line should be printed on the screen")
    elif 1 + 1 == 2:
        print("My condition is also true!")
    else:
        print("Or this?")

    print("Ah. We've reached the end of our program")


    # Working with while loops
    # How many times is the message "Python is cool" printed on the screen?
    counter = 1
    while counter <= 10:
        print("Python is cool")
        counter = counter + 1


    # Does it get simpler with a for loop?
    # Let n = 10, let's print the following message n times
    n = 10
    for _ in range(10):
        print("for loop is simple")

    # is_prime
    def is_prime(n: int):
        # 0, 1 are not prime numbers
        if n <= 1:
            return False
        # 2 is a prime number
        if n == 2:
            return True

        # other even numbers are not prime
        if n % 2 == 0:
            return False

        # if there exists an integer 1 < i < n such that
        # n is divisible by i, then n is not a prime number
        limit = math.floor(math.sqrt(n)) + 1
        for i in range(3, limit, 2):
            if n % i == 0:
                return False

        # if we cannot find such i, n is a prime number
        return True

    # go over this code, what prints out?
    a = "a"
    b = "b"
    c = "c"
    if a:
        print(a)
    if b == b:
        if 3 == 3.0 and a == 'a':
            print("1")
        if 5 == 6:
            print(1.1)
        else:
            if 4 == 5 or True:
                print(2)
                if not(True and False):
                    print("3")
            else:
                print(4)
    else:
        print(5)


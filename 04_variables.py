#!/usr/bin/env python3

"""This file contains example code for using variables in Python
"""


# Let's create new variables
x = 5
y = 10.0
s = 'i am a string literal'
print(x, y)     # 5 10.0
print(s)        # i am a string literal

# A new variable can be assigned the value of an existing variable
z = x
print(x, y, z)  # 5 10.0 5
print(s)        # i am a string literal

# What if we want to change x's value?
x = 42
print(x, y, z)  # 42 10.0 5
print(s)        # i am a string literal

# What if we want to use the value of x in an operation?
print( x * 1 )  # 42
print( x == 1 ) # False

# A variable has a type, which is the same as its value,
# and it can change depending on the type of the value
print(x, type(x))   # 42 <class 'int'>
print(y, type(y))   # 10.0 <class 'float'>
print(s, type(s))   # i am a string literal <class 'str'>

x = "now i'm no longer an int type"
print(x, type(x))   # now i'm no longer an int type <class 'str'>

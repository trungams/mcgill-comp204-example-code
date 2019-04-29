#!/usr/bin/env python3

"""This file contains example code for basic types in Python,
including conversion between numeric types and strings
"""

import math


# In order to find out the type of a literal or a variable, use the type() function,
# along with print() to display the result


# Numeric types, including integers (int) and floating point numbers (float)

# Integers (int)
print( type(10) )   # int
print( type(0) )    # int
print( type(-1) )   # int

# Floats (float)
print( type(2.0) )  # float
print( type(1e9) )  # float
print( type(math.pi) )  # float


# Boolean type (bool), which is simply 0 (False) and 1 (True) under the hood
# Don't forget to capitalize the first letter
print( type(True) ) # bool


# String type (str), which is a contiguous sequence of characters in memory
print( type('hello, world!') )  # str
print( type("it's possible to use double quotes to wrap around a string") ) # str
print( type("""triple quotes are not just used for commenting!""") )    # str


# Type conversions

# Other types -> Integers
print( int(1) )     # int -> int
print( int(1.0) )   # float -> int
print( int(False) ) # bool -> int
print (int('12') )  # str -> int
print( int('101010101011111', 2) )  # 21855, since it's doing a binary -> decimal conversion

# Other types -> Floats
print( float(1) )       # int -> float
print( float(False) )   # bool -> float
print( float('42.0') )  # str -> float

# Other types -> Strings
print( str(1) )     # returns the string '1'
print( str(True) )  # returns the string 'True'
print( str(42.0) )  # returns the string '42.0'

# Other types -> Boolean
print( bool(1) )        # True
print( bool(0.0000) )   # False
print( bool('True') )   # True
print( bool('False') )  # True, can you explain why? Hint: look at the example below
print( bool('') )       # False. '' represents an empty string


# and many more types (built-in or user-defined) are supported in Python!
print( type([]) )       # list
print( type({1,2,3}) )  # set
print( type({1: 'a'}) ) # dict


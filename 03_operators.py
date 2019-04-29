#!/usr/bin/env python3

"""This file contains example code for basic operators in Python,
including arithmetic, boolean, string, binary operators, comparisons
"""


# We start with simple arithmetic operators
print( 40 + 2 )         # addition
print( 3.14 - 0.004 )   # subtraction
print( 6 / 2 )          # always float division, result is 3.0 (float)
print( 6 // 2 )         # floor division, result is 3 (int)
print( 10 * 0.2 )       # multiplication
print( 3 % 2 )          # modulus
print( 2**31 )          # exponentiation
print( (10 + 2) * 3**0 )        # precedence rules apply, result is 12
# Commutative, associative, and distributive rules apply as well


# Boolean operators (we only deal with 2 boolean literals: True-False right now)
print( True and True )
print( False or True )
print( not True )
print( not True and False )
print( not (True and False) )


# String operators
print( 'hello' + " there" )     # remember you can alternate single and double quotes to wrap string literals
print( 'h' + 'i' * 10 )         # when you meet your close friend after a year C:


# Comparisons
print( 1 == 1 )
print( 2.4 >= 2 )
print( 1 is 10 )
print( 42 is not 24 )
print( True is False )
print( 'this' is 'this' )
print( 'a' < 'b' )          # do you know why? (hint: look up the ASCII values of lowercase a and b)


# Some more advanced stuffs
print( 1 is 1 )             # True
print( 1 == 1.0 )           # True
print( 1 is 1.0 )           # False, the values are equal but types are not
print( 1 == 0.999999999999999999999 )   # This turns out to be True! But it's very tricky, you don't need to remember it
print( '1000' < '6' )       # be careful! We are comparing string literals here, not numbers!

# Binary operators
print( 1 & 1 )              # 1. This is very similar to "True and True"
print( 0 | 1 )              # 1. What number represents the boolean False under the hood?
print( 10 ^ 20 )            # 30. Convert 10 and 20 to binary first


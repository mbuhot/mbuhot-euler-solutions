#! /usr/bin/env python3

from math import sqrt
from decimal import getcontext, Decimal

description = '''
Square root digital expansion
Problem 80
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
'''

# set the decimal precision slightly above the required 100, so there isn't any rounding in the last digit
getcontext().prec = 110

# sum the digits, excluding '.'
def decimalSum(d):
  digits = str(d)[:101]
  return sum(int(c) for c in digits if c != '.') 

assert(decimalSum(Decimal(2).sqrt()) == 475)

def isSquare(n):
  return sqrt(n).is_integer()

total = sum(decimalSum(Decimal(n).sqrt()) for n in range(1, 101) if not isSquare(n))
print(total)

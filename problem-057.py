#! /usr/bin/env python3

from fractions import Fraction
from memo import memoize
from itertools import count, islice

description = '''
Square root convergents
Problem 57
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
'''

@memoize
def f(n):
  if n == 0: return 0
  return Fraction(1, 2 + f(n-1))

def sqrt2(n):
  return 1 + f(n)

assert(sqrt2(1) == Fraction(3,2))
assert(sqrt2(2) == Fraction(7,5))
assert(sqrt2(3) == Fraction(17,12))
assert(sqrt2(4) == Fraction(41,29))

root2s = (sqrt2(n) for n in count(1))
biggerNumerators = [f for f in islice(root2s, 1000) if len(str(f.numerator)) > len(str(f.denominator))]

print(len(biggerNumerators),'have a bigger numerator')
  

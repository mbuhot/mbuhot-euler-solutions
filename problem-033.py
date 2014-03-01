#! /usr/bin/env python3

description = """
Digit canceling fractions
Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

import fractions

def commonDigit(a, b):
  d1 = a % 10
  d2 = a // 10
  if (d1 == b % 10 and d1 != 0): return d1
  elif (d2 == b % 10): return d2
  elif (d1 == b // 10): return d1
  elif (d2 == b // 10): return d2
  else: return None

def removeDigit(n, d):
  d1 = n % 10
  d2 = n // 10
  return d2 if (d1 == d) else d1

assert(commonDigit(49,98) == 9)
assert(removeDigit(49, 9) == 4)
assert(removeDigit(98, 9) == 8)
assert(49 / 98 == removeDigit(49, 9) / removeDigit(98, 9)) 

commonDigitNumbers = ((a, b) for a in range(11, 100) 
                             for b in range(a+1, 100) 
                             if commonDigit(a,b) is not None)

def digitCancellingFractions():
  for (numerator, denominator) in commonDigitNumbers:
    d = commonDigit(numerator, denominator)
    n1 = removeDigit(numerator, d)
    d1 = removeDigit(denominator, d)
    if d1 != 0 and (numerator / denominator) == (n1 / d1):
      yield fractions.Fraction(numerator, denominator)

result = 1
for f in digitCancellingFractions():
  result = result * f

print('product of digit cancelling fractions:', result)


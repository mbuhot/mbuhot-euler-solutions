#! /usr/bin/env python3

from itertools import chain

description = """
Pandigital products
Problem 32
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

def pandigitalProduct(i, j):
  return "".join(sorted(str(i) + str(j) + str(i*j))) == "123456789"

assert(pandigitalProduct(39, 186))

def pandigitals(irange, jrange):
  return (i*j for i in range(irange, irange*10) 
              for j in range(jrange, jrange*10)
              if pandigitalProduct(i,j))

# for 9 digits total, we can only have:
#   1 digit  * 4 digits = 4 digits (1 + 4 + 4 = 9)
#   2 digits * 3 digits = 4 digits (2 + 3 + 4 = 9)
results = set(chain(pandigitals(1, 1000), pandigitals(10, 100)))

print(sum(results))

#! /usr/bin/env python3

from math import factorial

description = """
Digit factorials
Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

def sumDigitFactorials(n):
  total = 0
  while (n > 0):
    total += factorial(n % 10)
    n = n // 10
  return total

assert(145 == sumDigitFactorials(145))

# 7 * 9! is a 7 digit number, so that is as far as needed to search
m = 7 * factorial(9)
numbers = (x for x in range(3, m+1) if x == sumDigitFactorials(x))
print(sum(numbers))
  

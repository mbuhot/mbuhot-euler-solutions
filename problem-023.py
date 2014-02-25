#! /usr/bin/env python3

import itertools
import factorization

description = """
Non-abundant sums
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def is_abundant(n):
  return sum(factorization.divisors(n)[:-1]) > n

assert(is_abundant(12))
assert(not is_abundant(14))

def abundant_numbers(maxval):
  return (i for i in range(1, maxval+1) if is_abundant(i))

def abundant_sums(maxval):
  a = list(abundant_numbers(maxval))
  result = {}
  for x in a:
    for y in a:
      n = x + y
      if n > maxval: break
      result[x+y] = True
  return result

abundantSums = abundant_sums(28123)
nonAbundantSums = [x for x in range(1, 28123 + 1) if not x in abundantSums]

print('Sum of numbers which cannot be expressed as sum 2 abundant numbers:', sum(nonAbundantSums)) 

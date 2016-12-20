#! /usr/bin/env python3

import math

description = """
Sub-string divisibility
Problem 43
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

def isPandigital(n):
  return ''.join(sorted(str(n))) == '0123456789'

def anyRepeatedDigits(n):
  counts = [0] * 10
  while n > 0:
    d = n  % 10
    counts[d] += 1
    if counts[d] > 1: return True
    n = n // 10
  return False


steps = [1, 2, 3, 5, 7, 11, 13, 17]
def generator(k=0, n=0):
  if k == len(steps):
    if isPandigital(n): 
      yield n
    return

  for d in range(0 if k > 0 else 1, 1000, steps[k]):
    n2 = (n // 100) * 1000 + d
    if ((k > 0) and (n % 100) != (d // 10)) or anyRepeatedDigits(n2): 
      continue

    for result in generator(k+1, n2):
      yield result    

result = list(generator())
assert(1406357289 in result)
print('pandigitals with prime divisors in digit groups:', result)
print('sum of results:', sum(result))

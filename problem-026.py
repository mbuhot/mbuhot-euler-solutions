#! /usr/bin/env python3

from itertools import takewhile, count
from prime import primes

description = """
Reciprocal cycles
Problem 26
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

def geometricSeries(a, r):
  sum = 0
  while True:
    sum += a
    yield sum
    a *= r

def nines(): 
  return geometricSeries(a=9, r=10)

def digitCycle(p):
  for i, n in zip(range(1,p), nines()):
    if n % p == 0:
      return i
  return 0

primesTo1000 = takewhile(lambda x: x < 1000, primes())
result = max(primesTo1000, key=digitCycle)

print('1/%d has digit cycle length %d' % (result,digitCycle(result)))


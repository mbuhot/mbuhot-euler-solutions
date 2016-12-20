#! /usr/bin/env python3

import itertools
import prime
from memo import memoize

description = '''
Spiral primes
Problem 58
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
'''


@memoize
def primediagonals(n):
  if n == 1: return 0
  m = n - 1
  return primediagonals(n-2) + sum(1 for x in (n*n - k*m for k in (3,2,1,0)) if prime.isPrime(x)) 

assert(primediagonals(7) == 8)

def primeratio(n):
  total = 2*n - 1
  return primediagonals(n) / total

for n in itertools.count(3, step=2):
  if primeratio(n) < 0.1:
    print('prime ratio for length',n,'is',primeratio(n))
    break


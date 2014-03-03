#! /usr/bin/env python3

from itertools import count, takewhile, filterfalse
from prime import isPrime, isComposite

description = '''
Goldbach's other conjecture
Problem 46
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

odds = count(start=3, step=2)
compositeOdds = filter(isComposite, odds)

def squares(max):
  return takewhile(lambda x: x <= max, (i*i for i in count(1)))

def Goldbach(n):
  return any(isPrime(x) for x in (n - 2*sq for sq in squares(n/2)))

assert(all(Goldbach(n) for n in [9, 15, 21, 25, 27, 33]))

print(next(filterfalse(Goldbach, compositeOdds)))


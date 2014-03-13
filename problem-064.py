#! /usr/bin/env python3

import math
import itertools

description = '''
Odd period square roots
Problem 64

Exactly four continued fractions, for N ≤ 13, have an odd period.
How many continued fractions for N ≤ 10000 have an odd period?
'''

def repeat(N, a, b, c, seen):
'''Yield successive 'a' values until repetition detected
   xi = ai + b / (sqrt(N) - c)'''

  while not (a,b,c) in seen:
    seen.add((a,b,c))
    yield a

    d = N - c*c
    anext = math.floor(b * (math.sqrt(N) + c) / d)
    cnext = -(c - anext * d / b)
    bnext = d / b
    a, b, c = anext, bnext, cnext
  
def sqrt(N):
  a = math.floor(math.sqrt(N))
  b = 1
  c = a
  return repeat(N,a,b,c,set())

def period(n):
  return sum(1 for a in sqrt(n)) - 1

oddPeriod = [n for n in range(1, 10000) 
               if not math.sqrt(n).is_integer() 
               and (period(n) % 2 == 1)]

print(len(oddPeriod))

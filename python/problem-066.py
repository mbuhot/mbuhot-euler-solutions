#! /usr/bin/env python3

import itertools
import math
from fractions import Fraction

description = '''
Diophantine equation
Problem 66
Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
'''

# From Wikipedia's page on Pells Equation: Let hi / ki denote the sequence of convergents to the continued fraction for sqrt(n).
# Then the pair (x1,y1) solving Pell's equation and minimizing x satisfies x1 = hi and y1 = ki for some i.  

def repeat(N, a, b, c):
  '''Yield successive 'a' values until repetition detected xi = ai + b / (sqrt(N) - c)'''
  while True:
    yield a
    d = N - c*c
    anext = math.floor(b * (math.sqrt(N) + c) / d)
    bnext = d / b
    cnext = anext * bnext - c
    a, b, c = anext, bnext, cnext
  
def sqrt(N):
  a = math.floor(math.sqrt(N))
  b = 1
  c = a
  return repeat(N,a,b,c)

def convergent(seq, n):
  a = next(seq)
  if n == 1: return a
  else: return a + Fraction(1, convergent(seq, n-1))

def solve(d):
  for i in itertools.count(1):
    f = convergent(sqrt(d), i)
    x = f.numerator
    y = f.denominator
    if (x*x - d*y*y) == 1: 
      return x 

assert(solve(2) == 3)
assert(solve(3) == 2)
assert(solve(5) == 9)
assert(solve(6) == 5)
assert(solve(7) == 8)

solutions = [(d,solve(d)) for d in range(2, 1000) if not math.sqrt(d).is_integer()]
print(max(solutions, key=lambda pr: pr[1]))

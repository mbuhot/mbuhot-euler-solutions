#! /usr/bin/env python3

import itertools
from fractions import Fraction

description = '''
Convergents of e
Problem 65

What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
'''

def eSeq():
  yield 2
  for k in itertools.count(1):
    yield 1
    yield 2*k
    yield 1

def convergent(seq, n):
  a = next(seq)
  if n == 1: return a
  else: return a + Fraction(1, convergent(seq, n-1))

assert(2 == convergent(eSeq(), 1))
assert(3 == convergent(eSeq(), 2))
assert(Fraction(8, 3) == convergent(eSeq(), 3))
assert(Fraction(11, 4) == convergent(eSeq(), 4))
assert(17 == sum(int(c) for c in str(convergent(eSeq(), 10).numerator)))

print(sum(int(c) for c in str(convergent(eSeq(), 100).numerator)))


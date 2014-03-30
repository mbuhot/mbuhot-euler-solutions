#! /usr/bin/env python3

from itertools import count
from memo import memoize
from math import sqrt, pi, exp
import prime

import sys
sys.setrecursionlimit(100000)

description = '''
Coin partitions
Problem 78
Let p(n) represent the number of different ways in which n coins can be separated into piles. 
For example, five coins can separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
'''

# from Mathworld:  P(n)=sum_(k=1)^n(-1)^(k+1)[P(n-1/2k(3k-1))+P(n-1/2k(3k+1))] 
# This ugly looking code is required for decent performance in python :( 
_P = [-1] * 100000
_P[0] = 1
_P[1] = 1
def P(n):
  if _P[n] < 0: 
    sign = 1
    total = 0
    for k in range(1, n+1):
       m1 = n - k*(3*k - 1)//2
       if m1 < 0: break
       total += sign * _P[m1]
       m2 = n - k*(3*k + 1)//2
       if m2 < 0: break
       total += sign * _P[m2]
       sign *= -1

    _P[n] = total
  return _P[n]

for n in range(0, len(_P)):
  Pn = P(n)
  if Pn % 1000000 == 0:
    print(n, P(n))
    break


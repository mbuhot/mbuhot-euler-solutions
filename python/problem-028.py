#! /usr/bin/env python3

description = """
Number spiral diagonals
Problem 28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

from itertools import islice


def spiralDiagonals(n):
  yield 1
  for x in range(3, n+1, 2):
    yield x*x - 3*(x-1)
    yield x*x - 2*(x-1)
    yield x*x - 1*(x-1)
    yield x*x

assert(sum(spiralDiagonals(5)) == 101)
print('sum of spiral diagonals length 1001:', sum(spiralDiagonals(1001)))

#! /usr/bin/env python3

import sys
from memo import memoize

sys.setrecursionlimit(10000)

description = '''
Maximum path sum II
Problem 67
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
'''

with open('triangle.txt') as f:
  numbers = [[int(s) for s in line.split(' ')] for line in f]

N = len(numbers)

@memoize
def maxPath(i,j):
  return numbers[i][j] + (max(maxPath(i+1, j), maxPath(i+1, j+1)) if i < N-1 else 0)
  
print('longest path is:', maxPath(0,0))

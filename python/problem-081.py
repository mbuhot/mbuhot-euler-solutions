#! /usr/bin/env python3

from memo import memoize
import sys

description = '''
Path sum: two ways
Problem 81
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.


131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331

Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
'''

sys.setrecursionlimit(10000)
with open('matrix.txt', 'r') as f:
  matrix = [[int(x) for x in line.strip().split(',')] for line in f]


def minPathFromStart(matrix):
  @memoize
  def minPath(i, j):
    neighbours = []
    if i < len(matrix) - 1: neighbours.append((i+1, j))
    if j < len(matrix[i]) - 1: neighbours.append((i, j+1))
    return matrix[i][j] + (min(minPath(ii, jj) for (ii,jj) in neighbours) if len(neighbours) > 0 else 0)
  return minPath(0, 0)

test = [
[131,	673,	234,	103,	18],
[201,	96,	342,	965,	150],
[630,	803,	746,	422,	111],
[537,	699,	497,	121,	956],
[805,	732,	524,	37,	331]]

print(minPathFromStart(test))
print(minPathFromStart(matrix))

#! /usr/bin/env python3

from memo import memoize
import sys

description = '''
Path sum: three ways
Problem 82
NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.


131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331

Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.
'''

sys.setrecursionlimit(10000)
with open('matrix-82.txt', 'r') as f:
  matrix = [[int(x) for x in line.strip().split(',')] for line in f]


def minPathFromStart(matrix):
  N = len(matrix)
  minPathTo = [[sum(matrix[i][:j+1]) for j in range(0, N)] for i in range(0, N)]
  
  def search(i, j, soFar):
    if soFar + matrix[i][j] <= minPathTo[i][j]:
      minPathTo[i][j] = soFar + matrix[i][j]
      if i > 0:
        search(i-1, j, minPathTo[i][j])
      if i < N - 1:
        search(i+1, j, minPathTo[i][j])
      if j < N - 1:
        search(i, j+1, minPathTo[i][j])

  for i in range(0, N):
    search(i, 0, 0)

  return min(minPathTo[i][-1] for i in range(0, len(matrix)))

test = [
  [131,	673,	234,	103,	18],
  [201,	96,	342,	965,	150],
  [630,	803,	746,	422,	111],
  [537,	699,	497,	121,	956],
  [805,	732,	524,	37,	331]]

print(minPathFromStart(test))
print(minPathFromStart(matrix))

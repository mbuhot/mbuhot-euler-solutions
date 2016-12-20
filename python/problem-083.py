#! /usr/bin/env python3

from memo import memoize
import sys

description = '''
Path sum: four ways
Problem 83
NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.


131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331

Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.
'''

sys.setrecursionlimit(10000)
with open('matrix-83.txt', 'r') as f:
  matrix = [[int(x) for x in line.strip().split(',')] for line in f]


def minPathFromStart(matrix):
  N = len(matrix)
  minPathTo = [[sum(matrix[0][:j+1]) + sum(matrix[k][j] for k in range(0,i+1)) for j in range(0, N)] for i in range(0, N)]
  
  def search(i, j, soFar):
    if soFar + matrix[i][j] <= minPathTo[i][j]:
      minPathTo[i][j] = soFar + matrix[i][j]
      if i > 0:
        search(i-1, j, minPathTo[i][j])
      if i < N - 1:
        search(i+1, j, minPathTo[i][j])
      if j < N - 1:
        search(i, j+1, minPathTo[i][j])
      if j > 0:
        search(i, j-1, minPathTo[i][j])
  search(0, 0, 0)
  return minPathTo[-1][-1]

test = [
  [131,	673,	234,	103,	18],
  [201,	96,	342,	965,	150],
  [630,	803,	746,	422,	111],
  [537,	699,	497,	121,	956],
  [805,	732,	524,	37,	331]]

print(minPathFromStart(test))
print(minPathFromStart(matrix))

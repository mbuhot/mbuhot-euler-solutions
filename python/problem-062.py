#! /usr/bin/env python3

import itertools
import collections

description = '''
Cubic permutations
Problem 62
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

def cubicPermutations(n):
  cubecount = collections.defaultdict(set)
  for cube in (i**3 for i in itertools.count(1)):
    key = int(''.join(sorted(str(cube), reverse=True)))
    cubecount[key].add(cube)
    if len(cubecount[key]) == n:
      return min(cubecount[key])

assert(cubicPermutations(3) == 41063625)
print(cubicPermutations(5))

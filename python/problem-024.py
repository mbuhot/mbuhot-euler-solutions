#! /usr/bin/env python3

import itertools

description = """
Lexicographic permutations
Problem 24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

def permutations(l):
  if len(l) == 1: 
    yield l
    return

  for i in range(0, len(l)):
    l[0], l[i] = l[i], l[0]
    for tlperm in permutations(l[1:]):
      yield [l[0]] + tlperm

assert(list(permutations([1,2,3])) == [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]])

perms = permutations(list(range(0, 10)))
millionth = next(itertools.islice(perms, 999999, None))

print('millionth permutation of 0123456789:', ''.join(str(n) for n in millionth))

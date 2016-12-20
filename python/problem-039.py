#! /usr/bin/env python3

from collections import defaultdict
from itertools import count

description = """
Integer right triangles
Problem 39
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

# map from triangle perimeter to set of (a,b,c) that can produce it
triangles = defaultdict(set)

# use Euclids formula to generate all pythagorean triples 
for n in count(1):

  # once 4n^2 exceeds 1000, a+b+c will also be >1000
  if (4 * n**2) > 1000: 
    break

  for m in count(n+1):
    a = m**2 - n**2
    b = 2 * m * n
    c = m**2 + n**2
    p = a+b+c
    if p > 1000: break
    # standardize the tuples so that a is the smaller side
    a, b = min(a,b), max(a,b)
    k = 1
    while p*k < 1000:
      s = triangles[p*k]
      s.add((a*k,b*k,c*k))
      triangles[p*k] = s
      k += 1

assert(len(triangles[120]) == 3)
assert((20,48,52) in triangles[120])
assert((24,45,51) in triangles[120])
assert((30,40,50) in triangles[120])

maxKey = max(triangles.keys(), key=lambda p:len(triangles[p]))
print(maxKey)

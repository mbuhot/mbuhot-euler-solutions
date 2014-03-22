#! /usr/bin/env python3

from collections import defaultdict
from itertools import count

description = '''
Singular integer right triangles
Problem 75
It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
'''

# map from triangle perimeter to set of (a,b,c) that can produce it
triangles = defaultdict(set)

MAX_WIRE = 1500000

# use Euclids formula to generate all pythagorean triples 
for n in count(1):

  # once 4n^2 exceeds MAX_WIRE, a+b+c will also be >MAX_WIRE
  if (4 * n**2) > MAX_WIRE: 
    break

  for m in count(n+1):
    a = m**2 - n**2
    b = 2 * m * n
    c = m**2 + n**2
    p = a+b+c
    if p > MAX_WIRE: break
    # standardize the tuples so that a is the smaller side
    a, b = min(a,b), max(a,b)
    k = 1
    while p*k <= MAX_WIRE:
      triangles[p*k].add((a*k,b*k,c*k))
      k += 1

print(sum(1 for (k,v) in triangles.items() if len(v) == 1))

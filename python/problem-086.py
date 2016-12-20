#! /usr/bin/env python3

from math import sqrt, ceil
from itertools import count
from pythagoras import pythagoreanTriples

description = '''
Cuboid route
Problem 86
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.


However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.

By considering all cuboid rooms with integer dimensions, up to a maximum size of M by M by M, there are exactly 2060 cuboids for which the shortest route has integer length when M=100, and this is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions is 1975 when M=99.

Find the least value of M such that the number of solutions first exceeds one million.
'''


# shortest path is given by sqrt(w^2 + (d + h)^2) 
# which is intuitive if you imagine the room flattened out
# The integer solutions to this are pythagorean triples.
# Re-using the code developed for a previous problem, generate the triples having max perimeter = 5*M.
# a < b < c
# When b <= M, then width = b, and there are a/2 combinations for depth and heigh
# When a <= M and 2a >= b, then width = a and there are ceil(2a-b+1)/2 combinations for depth and height

def integerCuboidRoutes(M):
  count = 0
  for (a,b,c) in pythagoreanTriples(5*M):
    if b <= M:
      count += a // 2
    if a <= M and a >= b/2:
      count += ceil((2*a - b + 1) / 2)  
  return count

for M in count(1):
  c2 = integerCuboidRoutes(M)
  if c2 > 1000000:
    print(M, c2)
    break

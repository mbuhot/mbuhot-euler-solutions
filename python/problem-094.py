#! /usr/bin/env python3

from fractions import gcd
from math import sqrt, floor, ceil

description = '''
Almost equilateral triangles
Problem 94
It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).
'''


'''
From Wikipedia:
All isosceles Heronian triangles are given by rational multiples of
a = 2(u^2-v^2),
b = u^2+v^2,
c = u^2+v^2,
for coprime integers u and v with u>v.

We want a to be approximately equal to b, so:

2(u**2 - v**2) = u**2 + v**2
2u^2 - 2v^2 = u^2 + v^2
u^2 = 3v^2
u / sqrt(3) = v
'''

def coprime(u): 
  return lambda v: gcd(u,v) == 1

def heronianTriangles(maxPerimeter):
  for u in range(2, ceil(sqrt(maxPerimeter))):
    vapprox = u / sqrt(3)
    for v in filter(coprime(u), [floor(vapprox), ceil(vapprox)]):
      a1 = 2*(u*u - v*v)
      b1 = u*u + v*v
      div = gcd(a1, b1)
      a, b = a1//div, b1//div

      if abs(a-b) == 1 and (a+b+b) <= maxPerimeter:
        yield (a,b,b)

print(sum((a+b+c) for (a,b,c) in heronianTriangles(int(1e9))))


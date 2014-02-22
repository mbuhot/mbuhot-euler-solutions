#! /usr/bin/env python3

# Special Pythagorean triplet
#Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def BruteForceSolution():
  for a in range(1, 1000):
    for b in range(a, 1000):
      c = 1000 - b - a
      if a*a + b*b == c*c:
        return a*b*c

print("Brute force solution:", BruteForceSolution())

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
 

#Euclids formula:
# for all m and n with m > n. The formula states that the integers
# a = m^2 - n^2, b = 2mn, c = m^2 + n^2
# are a pythagorean triple
#
# We have 
#   1000 = a + b + c 
#        = 2m^2 + 2mn
# => 500 = m^2 + mn
#        = m(m + n)
# factors of 500 are: 1, 2, 4, 5, 10, 20, 25, 50, 100, 125, 250, 500
# only 20 x 25 fits: m(m+n), for m > n: m = 20, n = 5
def MathSolution():
  m = 20
  n = 5
  a = m*m - n*n
  b = 2 * m *n
  c = m*m + n*n 
  assert(a*a + b*b == c*c)
  assert(a + b + c == 1000)
  return a*b*c

print("Brute force solution:", BruteForceSolution())
print("Math solution: ", MathSolution())

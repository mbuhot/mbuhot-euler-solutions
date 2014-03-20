#! /usr/bin/env python3

import array

description = '''
Counting fractions
Problem 72
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
'''

# From wikipedia: http://en.wikipedia.org/wiki/Farey_sequence
# |Fn| = 1 + sum(phi(m) for m in 1..n)
# But Euler excludes 0/1 and 1/1, so we use sum(phi) - 1

# Inspired by sieve of eratosthenes, calculate Phi(n) for all n in 0..N
# incrementally calculates Phi(n) = n * product(1 - 1/p for p in factors(n))
def phisieve(N):
  phi = array.array('l', range(0, N + 1))
  for i in range(2, len(phi)):
    if phi[i] == i: # i is prime
      for j in range(i, len(phi), i):
        phi[j] = (phi[j] * (i-1)) // i
  return phi

def fareylen(N):
  return sum(phisieve(N)) - 1

assert(fareylen(8) == 21)
print(fareylen(1000000))


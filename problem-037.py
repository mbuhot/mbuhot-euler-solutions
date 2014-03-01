#! /usr/bin/env python3

import prime
from itertools import islice

description = """
Truncatable primes
Problem 37
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

def isTruncatable(p):
  if p < 10: return False
  strp = str(p)
  ps = [int(strp[i:]) for i in range(1, len(strp))] + [int(strp[:i]) for i in range(1, len(strp))]
  return all(prime.isPrime(x) for x in ps)

assert(isTruncatable(3797))
assert(not isTruncatable(5))
assert(not isTruncatable(41))

truncatablePrimes = (p for p in prime.primes() if isTruncatable(p))
print(sum(islice(truncatablePrimes, 11)))

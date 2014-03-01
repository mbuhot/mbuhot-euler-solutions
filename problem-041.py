#! /usr/bin/env python3

import prime
from itertools import permutations

description = """
Pandigital prime
Problem 41
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

def digitsToInt(l):
  return sum(d*10**i for (i,d) in enumerate(reversed(l)))

assert(digitsToInt([1,5,3,2,4]) == 15324)

pandigitals = (digitsToInt(perm)
                 for n in range(2, 10) 
                 for perm in permutations(range(1, n+1)))

primePandigitals = filter(prime.isPrime, pandigitals)
print(max(primePandigitals))

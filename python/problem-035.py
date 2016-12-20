#! /usr/bin/env python3

import prime
from itertools import takewhile

description = """
Circular primes
Problem 35
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

def rotations(n):
  ns = str(n)
  nd = len(ns)
  ns = ns * 2
  for i in range(0, nd):
    yield int(ns[i:i+nd])

assert(list(rotations(197)) == [197, 971, 719])

def isCircularPrime(i):
  for j in rotations(i):
    if not prime.isPrime(j):
      return False
  return True

assert(isCircularPrime(197))

circularPrimes = [p for p in prime.primes(1000000) if isCircularPrime(p)]
print(len(circularPrimes))



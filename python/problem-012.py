#! /usr/bin/env python3

import itertools
import functools

problem12 = """
Highly divisible triangular number
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

knownPrimes = [2]
compositeToPrime = {4 : 2}

def primes():
  """Prime generator"""
  for p in knownPrimes:
    yield p

  i = knownPrimes[-1] + 1
  while True:
    if not i in compositeToPrime:
      knownPrimes.append(i)
      compositeToPrime[i*i] = i
      yield i
    else:
      prime = compositeToPrime[i]
      nextComposite = i + prime
      while nextComposite in compositeToPrime:
        nextComposite += prime
      compositeToPrime[nextComposite] = prime
      del compositeToPrime[i]
    i += 1
      
primeFactorMemoized = { 1 : {} }
def primeFactors(n):
  """Use trial division of primes to find factors"""
  if n in primeFactorMemoized:
    return primeFactorMemoized[n].copy()

  for prime in primes():
    if (n % prime == 0):
      result = primeFactors(n // prime)
      result[prime] = result.setdefault(prime, 0) + 1
      primeFactorMemoized[n] = result
      return result.copy()

def triangleNumbers():
  i = 1
  n = i
  while True:
    yield n
    i += 1    
    n += i

def numFactors(n):
  primeFacs = primeFactors(n)
  numFacs = 1
  for exponent in primeFacs.values():
    numFacs = numFacs * (exponent + 1)
  return numFacs

assert([1, 3, 6, 10, 15, 21, 28] == list(itertools.islice(triangleNumbers(), 0, 7)))
assert(numFactors(1) == 1)
assert(numFactors(3) == 2)
assert(numFactors(6) == 4)
assert(numFactors(10) == 4)
assert(numFactors(15) == 4)
assert(numFactors(21) == 4)
assert(numFactors(28) == 6)

n = next((x for x in triangleNumbers() if numFactors(x) > 500))
print(n, "has", numFactors(n), "factors")

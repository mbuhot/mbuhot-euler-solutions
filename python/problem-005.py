#! /usr/bin/env python3

# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import operator

def primes():
  """Prime generator"""
  compositeToPrime = {}
  i = 2
  while True:
    if not i in compositeToPrime:
      yield i
      compositeToPrime[i*i] = i
    else:
      prime = compositeToPrime[i]
      nextComposite = i + prime
      while nextComposite in compositeToPrime:
        nextComposite += prime
      compositeToPrime[nextComposite] = prime
      del compositeToPrime[i]
    i += 1
      
def primeFactors(n):
  """Use trial division of primes to find factors"""
  result = {}
  for prime in primes():
    if (n == 1): return result
    while (n % prime == 0):
      result[prime] = result.setdefault(prime, 0) + 1 
      n = n // prime

def productOfFactors(factorDict):
  product = 1
  for (factor, exponent) in factorDict.items():
    product = product * pow(factor, exponent)
  return product

def smallestMultiple(divisors):
  factorizations = [primeFactors(n) for n in divisors]
  combinedFactors = {}
  for factorDict in factorizations:
    for (factor, exponent) in factorDict.items():
      combinedFactors[factor] = max(exponent, combinedFactors.setdefault(factor, 0))
  result = productOfFactors(combinedFactors)
  print("least common multiple of", divisors, "=", result)
  return result

assert(2520 == smallestMultiple(range(1, 11)))
smallestMultiple(range(1, 21))

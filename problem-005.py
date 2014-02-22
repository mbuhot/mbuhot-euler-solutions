#! /usr/bin/env python3

# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def primes():
  """Prime generator"""
  compositeToPrime = {}
  yield 2;
  compositeToPrime[4] = 2
  i = 3
  while True:
    if not i in compositeToPrime:
      yield i
      compositeToPrime[i*i] = i
    else:
      prime = compositeToPrime[i]
      compositeToPrime[i + prime] = i
      del compositeToPrime[i]
    i += 2
      
def primeFactors(n, result=None):
  """Use recursive trial division of primes to find factors"""
  if result is None: result = {}
  if (n == 1): return result
  for prime in primes():
    if (n % prime == 0):
      result.setdefault(prime, 0)
      result[prime] += 1 
      return primeFactors(n / prime, result)

def smallestMultiple(divisors):
  factorizations = [primeFactors(n) for n in divisors]
  combinedFactors = {}
  for factorDict in factorizations:
    for (factor, exponent) in factorDict.items():
      combinedFactors.setdefault(factor, 0)
      combinedFactors[factor] = max(exponent, combinedFactors[factor])
  
  result = 1
  for (prime, exponent) in combinedFactors.items():
    result = result * pow(prime, exponent)

  print("least common multiple of", divisors, "=", result)
  return result

assert(2520 == smallestMultiple(range(1, 11)))
smallestMultiple(range(1, 21))

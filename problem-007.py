#! /usr/bin/env python3

# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

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

def drop(n, it):
  for i in range(0, n):
    next(it)
  return it

def nthPrime(n):
  return next(drop(n-1, primes()))

assert(nthPrime(6) == 13)
print("The 10001st prime is:", nthPrime(10001))


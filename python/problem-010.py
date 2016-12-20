#! /usr/bin/env python3

# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

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

def takeWhile(it, pred):
  for x in it:
    if not pred(x):
     break
    else:
      yield x

def sumPrimesBelow(n):
  return sum(takeWhile(primes(), lambda x: x < n))

assert(sumPrimesBelow(10) == 17)
print("Sum of primes below 2000000:", sumPrimesBelow(2000000))

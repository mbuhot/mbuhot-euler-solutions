#! /usr/bin/env python3

import prime
from memo import memoize

description = '''
Next
Product-sum numbers
Problem 88
A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
'''

def firstFactor(n):
  for p in prime.primes():
    if n % p == 0: return p

def replaceTupleElement(tup, idx, val):
  return tuple((x if j != idx else val) for (j,x) in enumerate(tup))

@memoize
def factorizations(n):

  # inner generator, yields factorizations, but some may be duplicates
  def facgen(n):

    # base case: prime or 1, only 1 factorization
    if n == 1 or prime.isPrime(n):
      yield (n,)
      return

    # recursive case: peel off the first factor of n,
    # then combine with all factorizations of n/factor
    # Use memoization to avoid repeated factorization of previously seen numbers
    factor = firstFactor(n)
    for subfac in factorizations(n // factor):
      # combine by appending 
      yield (factor,) + subfac

      # combine by multiplying each element of subfactor by the first factor
      for i in range(0, len(subfac)):
          yield replaceTupleElement(subfac, i, subfac[i] * factor)

  # outer function collects all generated factorizations, returns the unique set
  return set(tuple(sorted(fac)) for fac in facgen(n))      


def sumMinProductSums(maxK):

  # the minimum N that is a product-sum number for set size K
  minimums = [0] * (maxK + 1)

  # min product-sum number for K cannot be greater than 2K
  for n in range(2, 2*maxK):

    # Test each factorization of n, for potential sum-product solutions
    for factorization in factorizations(n):

      # sum(factorization) = product(factorization), use 1's to pad the sum until both sides equal
      # sum(factorization) + padding1s = n
      # => padding1s = n - sum(factorization)
      # => k = len(factorization) + padding1s
      #      = len(factorization) + n - sum(factorization)
      k = len(factorization) + n - sum(factorization)

      # test and update the minimum 
      if k <= 1 or k >= len(minimums): continue
      if minimums[k] == 0 or n < minimums[k]:
        minimums[k] = n

  # sum the unique n's that were minimum product-sum numbers
  return sum(set(minimums))

print('sum:', sumMinProductSums(12000))



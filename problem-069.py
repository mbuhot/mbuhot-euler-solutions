#! /usr/bin/env python3

import prime
import factorization

description = '''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
'''

prime.loadPrimes('primes.bin')

def product(it):
  result = next(it)
  for x in it: result *= x
  return result

def phi(n):
  factors = factorization.primeFactors(n).keys()
  result = round(n * product(1 - (1/p) for p in factors))
  return result


assert(phi(2) == 1)
assert(phi(3) == 2)
assert(phi(4) == 2)
assert(phi(10) == 4)

# create the number less than 1000000 with most prime factors
# This will be co-prime to the least number of other values, maximizing n / phi(n)
n = 1
for p in prime.primes():
  if n * p > 1000000: break
  n *= p

print(n, phi(n), n / phi(n))


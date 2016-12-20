#! /usr/bin/env python3

import math
import prime
from itertools import count
from memo import memoize

description = '''
Prime summations
Problem 77
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
'''

@memoize
def numSumsDigitsMax(value, numTerms, maxTerm):
  # single term
  if numTerms == 1:
    return 1 if prime.isPrime(value) and value <= maxTerm else 0

  # all 2's
  if value == numTerms*2: 
    return 1

  # split into first term + remaining terms
  # max term in recursive call cannot be greater than first term
  maxFirstTerm = min(maxTerm, value - 2 * (numTerms - 1))
  primes = prime.primes(maxFirstTerm + 1)
  return sum(numSumsDigitsMax(value - firstTerm, numTerms - 1, firstTerm) for firstTerm in primes)

def numSumsDigits(n, d):
  return numSumsDigitsMax(n, d, n - 2*(d - 1))
  
def numSums(n):
  return sum(numSumsDigits(n, d) for d in range(2, n//2 + 1))
	
assert(numSums(10) == 5)

for i in count(2):
  ns = numSums(i)
  if ns > 5000: 
    answer = i
    print(i, ns)
    break

# A very slick solution from Math Overflow - credit to J.M. http://math.stackexchange.com/questions/89240/prime-partition
# Gives the total number of prime partitions, so need to subtract 1 in the case of n being prime
# Memoization still required due to the recursive calls in the summation
def sumOfPrimeFactors(n):
  return sum(p for p in prime.primes(n + 1) if n%p == 0)

@memoize
def primePartitions(n):
  return (sumOfPrimeFactors(n) + sum(sumOfPrimeFactors(j)*primePartitions(n-j) for j in range(1, n))) // n  

def primeSums(n):
  return primePartitions(n) - (1 if prime.isPrime(n) else 0)

assert(numSums(answer) == primeSums(answer))

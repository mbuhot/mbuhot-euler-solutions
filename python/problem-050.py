#! /usr/bin/env python3

from prime import primes, isPrime, knownPrimes
from itertools import islice, takewhile

description = '''
Consecutive prime sum
Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

def consecutiveSumPrimes(maxPrime):
  ps = list(takewhile(lambda x: x < maxPrime, primes()))
  for i in range(0, len(ps)):
    total = ps[i]
    for j in range(i+1, len(ps)):
      total += ps[j]
      if total > maxPrime: break
      if isPrime(total):
        count = j - i + 1
        yield (total, count)
 
maxPrime, maxCount = max(consecutiveSumPrimes(1000000), key=lambda pr: pr[1])
print('%d is the sum of %d consecutive primes' % (maxPrime, maxCount))

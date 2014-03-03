#! /usr/bin/env python3

from prime import isPrime
from itertools import islice

description = '''
Prime permutations
Problem 49
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

fourDigitPrimes = [i for i in range(1001, 10000, 2) if isPrime(i)]

def primePermutations():
  for i in range(0, len(fourDigitPrimes)):
    pi = fourDigitPrimes[i] 
    pistr = sorted(str(pi))
    for j in range(i+1, len(fourDigitPrimes)):
      pj = fourDigitPrimes[j]
      d = pj - pi
      pk = pj + d
      if isPrime(pk) and pistr == sorted(str(pj)) and pistr == sorted(str(pk)):
        yield '%d%d%d' % (pi,pj,pk)

print(list(islice(primePermutations(), 2)))

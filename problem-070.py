#! /usr/bin/env python3


description = '''
totient permutation
Problem 70
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
'''
import math
import prime
prime.loadPrimes('primes.bin')

def search(N):
  nmin, rmin = 0, 2
  for p1 in prime.primes(N // 2):
    for p2 in prime.primes(min(p1, N // p1)):
      n = p1 * p2
      phin = round(p1 * p2 * (1 - 1/p1) * (1 - 1/p2))
      r = n / phin
      if sorted(str(n)) == sorted(str(phin)) and r < rmin:
          nmin, rmin = n, r
  return nmin
        
print(search(10**7))

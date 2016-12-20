#! /usr/bin/env python3

from factorization import primeFactors
from itertools import count, islice

description = '''
Distinct primes factors
Problem 47
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''

def fourPrimeFactors(i): 
  return len(primeFactors(i)) == 4

for i in count(start=1, step=4):
  if fourPrimeFactors(i):
    n = i
    m = i
    while fourPrimeFactors(n-1): n -= 1
    while fourPrimeFactors(m+1): m += 1
    if (m - n) >= 3:
      print(n)
      break
      

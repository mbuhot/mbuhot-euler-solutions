#! /usr/bin/env python3

import prime
import bitset

description = '''
Prime power triples
Problem 87
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
'''


def primePowerTriples(M):
  s1 = bitset.makebitset(M, 0)
  count = 0
  for a in prime.primes():
   if a**2 >= M: 
    break
   for b in prime.primes():
    if a**2 + b**3 >= M: 
      break
    for c in prime.primes():
      n = a**2 + b**3 + c**4 
      if n >= M: 
        break
      elif bitset.getbit(s1, n) == 0:
        count += 1
        bitset.setbit(s1, n)

  return count

assert(primePowerTriples(50) == 4)
print(primePowerTriples(50000000))


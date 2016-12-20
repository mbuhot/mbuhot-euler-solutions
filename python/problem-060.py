#! /usr/bin/env python3

import prime

description = '''
Prime pair sets
Problem 60
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''

prime.loadPrimes('primes.bin')

def digitconcat(a, b):
  return int(str(a) + str(b))

def isconnected(a, b):
  return prime.isPrime(digitconcat(a,b)) and prime.isPrime(digitconcat(b,a))

def search(space, path, n):
  if len(path) == n: return path
  p = path[0]
  sspace = filter(lambda x: not x in path and isconnected(p,x), sorted(space))
  for c in sspace:
    r = search(sspace, [c]+path, n)
    if r is not None:
      return r

def findPairSets(n):
  for p in prime.primes():
    space = [p]
    for p2 in prime.primes(p):
      if isconnected(p, p2):
        space.append(p2)
    if len(space) >= n:
      r = search(space, [p], n)
      if r is not None: yield r

result = next(findPairSets(5))
print(result, sum(result))

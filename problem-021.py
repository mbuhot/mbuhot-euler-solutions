#! /usr/bin/env python3

description = """
Amicable numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

knownPrimes = [2]
compositeToPrime = {4 : 2}

def primes():
  """Prime generator"""
  for p in knownPrimes:
    yield p

  i = knownPrimes[-1] + 1
  while True:
    if not i in compositeToPrime:
      knownPrimes.append(i)
      compositeToPrime[i*i] = i
      yield i
    else:
      prime = compositeToPrime[i]
      nextComposite = i + prime
      while nextComposite in compositeToPrime:
        nextComposite += prime
      compositeToPrime[nextComposite] = prime
      del compositeToPrime[i]
    i += 1
      
primeFactorMemoized = { 1 : {} }
def primeFactors(n):
  """Use trial division of primes to find factors"""
  if n in primeFactorMemoized:
    return primeFactorMemoized[n].copy()

  for prime in primes():
    if (n % prime == 0):
      result = primeFactors(n // prime)
      result[prime] = result.setdefault(prime, 0) + 1
      primeFactorMemoized[n] = result
      return result.copy()


def divisors(n):
  def _divisors(p, e, i, n):
    if (i == len(p)):
      yield n
    else:
      for exponent in range(0, e[i] + 1):
        m = n * p[i] ** exponent
        for d in _divisors(p, e, i+1, m):
          yield d

  pfs = primeFactors(n)
  p = list(pfs.keys())
  e = list(pfs.values())
  d = list(_divisors(p, e, 0, 1))
  d.sort()
  return d

assert([1, 2, 4, 5, 10, 20] == list(divisors(20)))
assert([1] == list(divisors(1)))

table = {}
for i in range(1, 10000):
  d = divisors(i)
  sd = sum(d[:-1])
  table[i] = sd

assert(table[220] == 284)
assert(table[284] == 220)

amicable = [n for (n, sd) in table.items() if (sd != n) and (sd in table) and (table[sd] == n)]
print('sum of amicables:', sum(amicable))


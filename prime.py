import bisect
import math

knownPrimes = [2]
compositeToPrime = {4 : 2}

def primes(max=None):
  """Prime generator"""
  for p in knownPrimes:
    if max is not None and p > max:
      return
    yield p

  i = knownPrimes[-1] + 1
  while True:
    if not i in compositeToPrime:
      knownPrimes.append(i)
      compositeToPrime[i*i] = i
      if max is not None and i > max:
        return
      yield i
    else:
      prime = compositeToPrime[i]
      nextComposite = i + prime
      while nextComposite in compositeToPrime:
        nextComposite += prime
      compositeToPrime[nextComposite] = prime
      del compositeToPrime[i]
    i += 1

def isPrime(n):
  i = bisect.bisect_left(knownPrimes, n)
  if i < len(knownPrimes):
    return knownPrimes[i] == n
  else:
    sqrtN = math.sqrt(n)
    for p in primes():
      if n % p == 0: return False
      if p > sqrtN: return True

def isComposite(n):
  return not isPrime(n)


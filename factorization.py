import collections
import prime
      
primeFactorMemoized = { 1 : collections.defaultdict(int) }
def primeFactors(n):
  """Use trial division of primes to find factors"""
 
  if n in primeFactorMemoized:
    return primeFactorMemoized[n].copy()

  for p in prime.primes():
    if (n % p == 0):
      result = primeFactors(n // p)
      result[p] = result[p] + 1
      primeFactorMemoized[n] = result
      return result.copy()


def divisors(n):
  """Find all divisors of n"""

  def divisor_generator(primes, exponents, index, result):
    """Generate all divisors given prime factors"""
    if (index == len(primes)):
      yield result
    else:
      for exponent in range(0, exponents[index] + 1):
        for d in divisor_generator(primes, exponents, index+1, result * primes[index] ** exponent):
          yield d

  factorDict = primeFactors(n)
  primes = list(factorDict.keys())
  exponents = list(factorDict.values())
  return sorted(list(divisor_generator(primes, exponents, index=0, result=1)))

#assert([1, 2, 4, 5, 10, 20] == divisors(20))
assert([1] == divisors(1))


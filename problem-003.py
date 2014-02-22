#! /usr/bin/env python3

#Largest prime factor
#Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?


def primes():
  """Prime generator"""
  compositeToPrime = {}
  yield 2;
  compositeToPrime[4] = 2
  i = 3
  while True:
    if not i in compositeToPrime:
      yield i
      compositeToPrime[i*i] = i
    else:
      prime = compositeToPrime[i]
      compositeToPrime[i + prime] = i
      del compositeToPrime[i]
    i += 2
      
def primeFactors(n):
  """Use recursive trial division of primes to find factors"""
  for prime in primes():
    if (prime == n): 
      return [prime]
    elif (n % prime == 0): 
      return [prime] + primeFactors(n / prime)

def largestPrimeFactor(n):
  """Maximum prime factor"""
  factors = primeFactors(n)
  return max(factors)

# test against the example given in the problem
assert(29 == largestPrimeFactor(13195))

# now for real
N = 600851475143
print("largest prime factor of ", N, " = ", largestPrimeFactor(N))

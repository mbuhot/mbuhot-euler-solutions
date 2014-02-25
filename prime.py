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


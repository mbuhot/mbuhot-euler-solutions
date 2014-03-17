import bitset
import array
from itertools import count
import math
from os import stat

N = 8
knownPrimes = bitset.makebitset(8, init=0)
for p in [2,3,5,7]:
  bitset.setbit(knownPrimes, p)

def sieveMorePrimes(M):
  print('sieving primes up to',M)
  newbitset = bitset.makebitset(M, init=1)
  bitset.clearbit(newbitset, 0)
  bitset.clearbit(newbitset, 1)
  for i in range(2, math.ceil(math.sqrt(M)) + 1):
    if bitset.getbit(newbitset, i) == 1:
      for j in range(i*i, M, i):
        bitset.clearbit(newbitset, j)

  global N, knownPrimes
  N,knownPrimes = M, newbitset

def isPrime(x):
  if x >= N:
    sieveMorePrimes(2*x)
  return bitset.getbit(knownPrimes, x) == 1
  
def primes(max=None):
  if max is not None and N < max:
    sieveMorePrimes(max)
  yield 2
  for i in count(3, step=2):
    if max is not None and i >= max: break
    if isPrime(i): yield i

def isComposite(n):
  return not isPrime(n)

def savePrimes(filename):
  with open(filename, 'wb') as f:
    knownPrimes.tofile(f)

def loadPrimes(filename):
  global knownPrimes, N
  with open(filename, 'rb') as f:
    filesize = stat(filename).st_size
    knownPrimes = array.array('B')
    knownPrimes.fromfile(f, filesize)
    N = filesize * 8


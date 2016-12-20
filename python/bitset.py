import array
import itertools
from math import ceil

def makebitset(n, init=0):
  initbyte = 0 if init == 0 else 0xff
  return array.array('B', itertools.repeat(initbyte, ceil(n/8)))

def setbit(bitset, n):
  bitset[n // 8] |= (1 << (n%8))

def clearbit(bitset, n):
  bitset[n // 8] &= ~(1 << (n%8))

def getbit(bitset, n):
  return (bitset[n // 8] >> (n%8)) & 1


b = makebitset(256)
setbit(b, 234)
assert(getbit(b, 234) == 1)
assert(getbit(b, 123) == 0)
clearbit(b, 234)
assert(getbit(b, 234) == 0)


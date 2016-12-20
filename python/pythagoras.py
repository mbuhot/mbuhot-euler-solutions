from itertools import count
from fractions import gcd
  

def pythagoreanTriples(maxPerimeter):
  '''Use Euclids formula to generate pythagorean triples up to a maximum perimeter'''
  for n in count(1):

    # once 4n^2 exceeds maxPerimeter, a+b+c will also be >maxPerimeter
    if (4 * n*n) > maxPerimeter: 
      break

    for m in count(n+1):
      if (m+n) % 2 == 1 and gcd(m,n) == 1: # avoids repeated results (via project euler forum thread 75)
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2
        p = a+b+c
        if p > maxPerimeter: 
          break
        # standardize the tuples so that a is the smaller side
        a, b = min(a,b), max(a,b)
        k = 1
        while p*k <= maxPerimeter:
          yield (a*k,b*k,c*k)
          k += 1


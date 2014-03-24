#! /usr/bin/env python3

from memo import memoize

description = '''
Counting summations
Problem 76
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
'''

@memoize
def numSumsDigitsMax(value, numTerms, maxTerm):
  # single term
  if numTerms == 1:
    return 1 if value <= maxTerm else 0

  # all 1's
  if value == numTerms: 
    return 1

  # split into first term + remaining terms
  # max term in recursive call cannot be greater than first term
  maxFirstTerm = min(maxTerm, value - numTerms + 1)
  return sum(numSumsDigitsMax(value - firstTerm, numTerms - 1, firstTerm) for firstTerm in range(maxFirstTerm, 0, -1))

def numSumsDigits(n, d):
  return numSumsDigitsMax(n, d, n - d + 1)
  
def numSums(n):
  return sum(numSumsDigits(n, d) for d in range(2, n+1))

assert(numSums(5) == 6)
print('100 can be generated', numSums(100), 'ways')
  


#! /usr/bin/env python3

import collections

description = '''
Digit factorial chains
Problem 74
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
'''

def fac(n):
  r = 1
  for i in range(2, n+1): r *= i
  return r

def digitfac(n):
  return sum(fac(int(d)) for d in str(n))

assert(digitfac(145) == 145)
assert(digitfac(169) == 363601)

def chainlen(n):
  seen = []
  while not n in seen:
    seen.append(n)
    n = digitfac(n)
  return len(seen)
    
assert(chainlen(69) == 5)

results = {}
histogram = collections.defaultdict(int)
for i in range(1, 1000000):
  key = int(''.join(sorted(str(i), reverse=True)))
  if not key in results:
    results[key] = chainlen(key)
  histogram[results[key]] += 1

print(histogram[60])

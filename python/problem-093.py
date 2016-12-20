#! /usr/bin/env python3

from itertools import permutations, combinations
from operator import add, mul, sub, truediv

description = '''
Arithmetic expressions
Problem 93
By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) − 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.
'''

def operators():
  for o1 in (add, mul, sub, truediv):
    for o2 in (add, mul, sub, truediv):
      for o3 in (add, mul, sub, truediv):
        yield (o1, o2, o3)

def reachable(digits):
  r = set()
  for ops in operators():
    for nums in permutations(digits):
      try: 
        res1 = ops[2](ops[1](ops[0](nums[0], nums[1]), nums[2]), nums[3]) 
      except ZeroDivisionError: 
        res1 = 0
      
      try: 
        res2 = ops[1](ops[0](nums[0], nums[1]), ops[2](nums[2], nums[3])) 
      except ZeroDivisionError: 
        res2 = 0
      
      try: 
        res3 = ops[2](ops[0](nums[0], ops[1](nums[1], nums[2])), nums[3]) 
      except ZeroDivisionError: 
        res3 = 0
      
      r.add(res1)
      r.add(res2)
      r.add(res3)

  n = 1
  while n in r:
    n += 1
  return n-1

results = [(digits, reachable(digits)) for digits in combinations(list(range(0, 10)), 4)]
maxResult = max(results, key=lambda x: x[1])
print(maxResult)  

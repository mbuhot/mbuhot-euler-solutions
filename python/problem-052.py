#! /usr/bin/env python3

from itertools import count

description = '''
Permuted multiples
Problem 52
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

def digitStr(i):
  return ''.join(sorted(str(i)))

def multiplesShareDigits(i):
  ds = digitStr(i)
  return all(digitStr(x) == ds for x in [i*2, i*3, i*4, i*5, i*6]) 

answers = (i for i in count(1) if multiplesShareDigits(i))
print(next(answers))

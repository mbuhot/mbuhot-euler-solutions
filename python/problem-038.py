#! /usr/bin/env python3

from itertools import count

description = """
Pandigital multiples
Problem 38
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

def pandigital(x):
  return "".join(sorted(str(x))) == "123456789"

def concatenatedProduct(i, r):
  return int("".join(str(i * n) for n in r))

assert(concatenatedProduct(192, range(1,4)) == 192384576)

def concatenatedProducts():
  for n in range(2, 10):
    for i in count(1):
      x = concatenatedProduct(i, range(1, n+1))
      if x > 987654321: 
        break
      if pandigital(x):
        yield x

print(max(concatenatedProducts()))


#! /usr/bin/env python3

from itertools import count

description = """
Digit fifth powers
Problem 30
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits
"""

def digits(n):
  while (n > 0):
    yield n % 10
    n = n // 10

digitPowers = [[d**n for d in range(0,10)] for n in range(0,10)]
def digitPowerSum(x, n):
  pows = digitPowers[n]
  return sum(pows[d] for d in digits(x))

for x in [1634, 8208, 9474]:
  assert(digitPowerSum(x, 4) == x)


# there is no 7 digit number that can be written as the sum of fifth powers of digits:
# 7 * 9 ** 5 = 413343, which only has 6 digits
# So limit the search to 6 digit numbers, up to 6 * 9 **5 = 354294
values = [i for i in range(2, 6 * 9 ** 5) if i == digitPowerSum(i,5)]
print(values)
print('sum: ', sum(values))


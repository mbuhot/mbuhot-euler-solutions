#! /usr/bin/env python3

description = """
Factorial digit sum
Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def factorial(n):
  result = 1
  for i in range(2, n+1):
    result = result * i
  return result

def digitSum(n):
  return sum(int(c) for c in str(n))

assert(factorial(5) == 5*4*3*2)
assert(digitSum(1234) == 1+2+3+4)
print('digitSum 100! =', digitSum(factorial(100)))


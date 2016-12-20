#! /usr/bin/env python3

import itertools
import math

description = """
Next
1000-digit Fibonacci number
Problem 25
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

def fibonaccis():
  a = 1; yield a;
  b = 1; yield b;
  while True:
    a, b = b, (a+b)
    yield b

def digitcount(n):
  return math.ceil(math.log10(n+1))

fibonacci_counts = zip(fibonaccis(), itertools.count(1))
largeFibs = itertools.dropwhile(lambda pr: digitcount(pr[0]) < 1000, fibonacci_counts)
print('First fibonacci with 1000 digits:', next(largeFibs)[1])

#! /usr/bin/env python3

description = """
Double-base palindromes
Problem 36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def doubleBasePalindromic(n):
  base10str = str(n)
  base2str = "{0:b}".format(n)
  return (base10str == base10str[-1::-1]) and (base2str == base2str[-1::-1])

assert(doubleBasePalindromic(585))
assert(not doubleBasePalindromic(11))
assert(not doubleBasePalindromic(15))

print(sum(i for i in range(1, 1000000) if doubleBasePalindromic(i)))


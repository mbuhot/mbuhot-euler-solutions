#! /usr/bin/env python3

#Largest palindrome product
#Problem 4
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(s):
  return s == s[::-1]
  
def BruteForceSolution(numDigits):
  result = 0
  lower = pow(10, numDigits - 1)
  upper = pow(10, numDigits)
  for i in range(lower, upper):
    for j in range(i, upper):
      prod = i * j
      if prod > result and isPalindrome(str(prod)):
        result = prod
  print("Largest palindrome from product of 2", numDigits, "digit numbers is:", result)
  return result

# Test isPalendrome helper function
assert(isPalindrome("abcdefgfedcba"))

# Test brute force solution with example from problem
assert(BruteForceSolution(2) == 9009)

# now for real
BruteForceSolution(3)

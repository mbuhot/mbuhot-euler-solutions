#! /usr/bin/env python3

# Sum square difference
# Problem 6

# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def BruteForceSolution(N):
  sumOfSquares = sum(i*i for i in range(1,N+1))
  squareOfSum = pow(sum(range(1, N+1)), 2)
  diff = squareOfSum - sumOfSquares
  print("Brute force solution: ", diff)
  return diff

def MathSolution(N):
  """Use sum of squares formula and sum of integers formula for O(1) solution"""
  sumOfSquares = N * (N+1) * (2*N + 1) // 6
  squareOfSum = pow((N + 1) * N // 2, 2)
  diff = squareOfSum - sumOfSquares
  print("Math solution: ", diff)
  return diff

assert(BruteForceSolution(10) == 2640)
assert(MathSolution(10) == 2640)
BruteForceSolution(100)
MathSolution(100)

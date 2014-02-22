#! /usr/bin/env python3

#if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def BruteForceSolution():
  multiplesOf3 = range(3, 1000, 3)
  multiplesOf5 = range(5, 1000, 5)
  multiplesOfBoth = range(3*5, 1000, 3*5)
  result = sum(multiplesOf3) + sum(multiplesOf5) - sum(multiplesOfBoth)
  print("Brute force result: %d" % result)

def MathSolution():
  def SumOfArithmeticSequence(a, n):
    return a * (n + 1) * n // 2
  
  multiplesOf3 = SumOfArithmeticSequence(3, 999 // 3)
  multiplesOf5 = SumOfArithmeticSequence(5, 999 // 5)
  multiplesOfBoth = SumOfArithmeticSequence(15, 999 // 15)
  result = multiplesOf3 + multiplesOf5 - multiplesOfBoth
  print("Math result: %d" % result)


BruteForceSolution()
MathSolution()

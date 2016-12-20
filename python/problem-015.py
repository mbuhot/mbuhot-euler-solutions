#! /usr/bin/env python3

description = """
Lattice paths
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

def factorial(n):
  result = 1
  for i in range(2, n+1):
    result = result * i
  return result

# there are 40 moves required to get from the top left to the bottom right of a 20 x 20 board
# we need to choose 20 of those moves to be horizontal, the other 20 must be vertical
# So using the combination formula for choosing r items from n items, order not important:
def binomialCoefficient(n, r):
  return factorial(n) / factorial(n-r) / factorial(r)

print(binomialCoefficient(40, 20), 'paths across the board')

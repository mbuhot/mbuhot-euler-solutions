#! /usr/bin/env python3

description = '''
Cube digit pairs
Problem 90
Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed:


In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?
'''

import itertools

def canMakeAllSquares(d1, d2):
  def canMakeSquare(n1, n2):
    return (n1 in d1 and n2 in d2) or (n1 in d2 and n2 in d1)

  return (canMakeSquare(0, 1) and
          canMakeSquare(0, 4) and
          (canMakeSquare(0, 9) or canMakeSquare(0, 6)) and
          (canMakeSquare(1, 6) or canMakeSquare(1, 9)) and
          canMakeSquare(2, 5) and
          (canMakeSquare(3, 6) or canMakeSquare(3, 9)) and
          (canMakeSquare(4, 9) or canMakeSquare(4, 6)) and
          (canMakeSquare(6, 4) or canMakeSquare(9, 4)) and
          canMakeSquare(8, 1))

count = 0
for d1 in itertools.combinations(list(range(0,10)), 6):
  for d2 in itertools.combinations(list(range(0,10)), 6):
    if canMakeAllSquares(d1, d2):
      count += 1

# half the count, as each combination repeated for the two die
print(count // 2)

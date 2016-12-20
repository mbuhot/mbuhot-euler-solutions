#! /usr/bin/env python3

import itertools

description = '''
Magic 5-gon ring
Problem 68
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.


Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?
'''


def issolution(p):
  # p[0:5] has the outer ring (each only counted once)
  # p[5:10] has the inner ring (each couted twice)
  s1 = p[0] + p[5] + p[6]
  s2 = p[1] + p[6] + p[7]
  s3 = p[2] + p[7] + p[8]
  s4 = p[3] + p[8] + p[9]
  s5 = p[4] + p[9] + p[5]
  # require that the lowest outer number is the first in sequence and
  # all sums equal, and 
  # 10 is in the outer ring (giving the required 16 digits)
  return p[0] == min(p[0:5]) and s1 == s2 and s2 == s3 and s3 == s4 and s4 == s5 and (10 in p[0:5])

def solutionstr(p):
  return int(('%d' * 15) % 
             (p[0], p[5], p[6], 
              p[1], p[6], p[7], 
              p[2], p[7], p[8],
              p[3], p[8], p[9],
              p[4], p[9], p[5])) 


# max 16 digit number will require 6, 10, 9, 8, 7 in the outer ring
# search permutations for inner 5 - could also be solved as linear system in 5 equations, but that would require scipy.
guesses = ([6, 10, 9, 8, 7] + list(p) for p in itertools.permutations(range(1, 5+1)))
solution = next(filter(issolution, guesses))
print(solutionstr(solution))


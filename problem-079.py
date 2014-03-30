#! /usr/bin/env python3

from collections import defaultdict

description = '''
Passcode derivation
Problem 79
A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
'''

#Note: Solution assumes no repeated digits in passcode

def findPrecedingDigit(endOfCode, lookup):
  for (digit, followingDigits) in lookup.items():
    if not digit in endOfCode and all(x in endOfCode for x in followingDigits):
      return digit
      
with open('keylog.txt', 'r') as f:
  logs = [[int(c) for c in line.rstrip()] for line in f]
  
lookup = defaultdict(set)
for line in logs:
  lookup[line[0]].add(line[1])
  lookup[line[1]].add(line[2])
  lookup[line[2]]

code = []
while True:
  first = findPrecedingDigit(code, lookup)
  if first is None: break
  code = [first] + code

print(code)


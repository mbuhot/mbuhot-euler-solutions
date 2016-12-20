#! /usr/bin/env python3

from math import log

description = '''
Largest exponential
Problem 99
Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
'''

# use the logarithm power rule to tame this problem:
# log(a**b) = b * log(a)
# And since log is an increasing function, log(a) > log(b) implies a > b
# So the max under log is the max overall.

maxLine, maxValue = 0, 0
with open('base_exp.txt', 'r') as f:
  for i,line in enumerate(f):
    parts = line.split(',')
    value = log(int(parts[0])) * int(parts[1])
    if value > maxValue:
      maxLine, maxValue = i+1, value

print(maxLine) 


#! /usr/bin/env python3

description = '''
Powerful digit counts
Problem 63
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

# 10**k has >k digits, so only need to look at numbers <10
# 9**21 is the last n-digit number which is an n-th power
assert(len(str(9**22)) < 22)

# count the list of n-digit nth powers 
print(sum(1 for d in range(1,10) for n in range(1,22) if len(str(d**n)) == n))

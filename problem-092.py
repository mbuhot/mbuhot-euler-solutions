#! /usr/bin/env python3

description = '''
Square digit chains
Problem 92
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''

count = 0  
cache = [0]*600 # after one iterator, all digit sums for n < 10,000,000 are < 600
for i in range(1, 10000000):
  chain = i
  while chain != 1 and chain != 89:
    x = chain
    digitSum = 0
    while x > 0:
      digit = x % 10
      digitSum += digit*digit
      x = x // 10
    chain = digitSum
    if cache[chain] > 0: 
      chain = cache[chain]
    
  if i < len(cache):
    cache[i] = chain

  if chain == 89: 
    count += 1
  
print(count)

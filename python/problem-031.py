#! /usr/bin/env python3

from itertools import dropwhile

description = """
Coin sums
Problem 31
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

coinValues = [1, 2, 5, 20, 50, 100, 200]

def coinCombinations(total, coins, idx=0, memo=dict()):
  """Memoizing coin combination generator"""
 
  if (total,idx) in memo: 
    return memo[(total,idx)]

  if total == 0:
    return 1

  elif idx == len(coins): 
    return 0

  else:
    coin = coins[idx]
    n = (total // coin) + 1
    result = memo[(total, idx)] = sum(coinCombinations(total - i*coin, coins, idx+1, memo) for i in range(0, n))
    return result

print(coinCombinations(200, [200, 100, 50, 20, 10, 5, 2, 1]))

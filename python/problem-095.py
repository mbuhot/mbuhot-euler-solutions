#!/usr/bin/env python3

description = '''
Amicable chains
Problem 95
The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
'''

# Pre-calculate all divisor sums up to 1000000
divisorSums = [0] * 1000001
for i in range(1, len(divisorSums)):
  j = 2*i
  while j < len(divisorSums):
    divisorSums[j] += i
    j += i

# returns (i, length of chain, min value in chain) for amicable chains
# or (i, 0, 0) for non-amicable chains
def chain(i):
  seen = []
  j = i
  while not j in seen and j < len(divisorSums):
    seen.append(j)
    j = divisorSums[j]  
  return (i, len(seen), min(seen)) if j == i else (i, 0, 0)

# find the longest chain
chains = map(chain, range(2, len(divisorSums)))
longest = max(chains, key=lambda x: x[1])

# print the min value
print(longest[2])


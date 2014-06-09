module problem131
  
description = """
Prime cube partnership

There are some prime values, p, for which there exists a positive integer, n, such that the expression n^3 + n^2 * p is a perfect cube.
For example, when p = 19, 8^3 + 8^2 × 19 = 12^3.
What is perhaps most surprising is that for each prime with this property the value of n is unique, and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?
"""

# By exhaustive search, I found the first few primes are 7, 19, 37, 61
# These are known as Cuban primes: primes of the form n^3 - (n-1)^3

function cubans(n = 1000000)
  x = 0
  for i = 2:n
    p = i^3 - (i-1)^3
    if p > n break
    elseif isprime(p) x += 1 end
  end
  return x
end

using Base.Test

@test cubans(100) == 4


                                                                                                                                                                                                                                                                
end
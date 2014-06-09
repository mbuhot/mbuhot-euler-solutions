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
#
# Insight after reading solutions from the ProjectEuler forums:
#
# n^3 + p * n^2 = k^3
# n^3 * (p/n + 1) = k^3
# n^3 * ((p+n)/n) = k^3
# n * cuberoot((p+n)/n) = k
# n * cuberoot(p+n) / cuberoot(n) = k
# For the cuberoot expressions to have integer results, p+n and n must be cubes.
# let n = x^3, p+n = y^3
# p = y^3 - x^3
# p = (y - x)(y^2 + xy + x^2)
# But p is required to be prime, so (y-x) must be 1 - otherwise (y-x) would be a factor of p.
# Therefore, p is the difference of consecutive cubes:
# p = y^3 - (y-1)^3
function cubans(n = 1000000)
  c = 0
  for y = 2:Inf
    p = y^3 - (y-1)^3
    if p > n 
      return c 
    elseif isprime(p) 
      c += 1 
    end
  end
end

using Base.Test
@test cubans(100) == 4
                                                                                                                                                                                                                                                             
end
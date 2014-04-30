module problem110

description = """
Diophantine reciprocals II

In the following equation x, y, and n are positive integers.
1/x + 1/y = 1/n

It can be verified that when n = 1260 there are 113 distinct solutions and this is the least value of n for which the total number of distinct solutions exceeds one hundred.
What is the least value of n for which the number of distinct solutions exceeds four million?
"""

# From the forums in problem 108, I found that the number of solutions to N = ((number of divisors of N^2) + 1)/2
# Number of divisors can be efficiently calculated by taking the product of (power+1) for the powers of the prime factors of n

function nextprime(n)
  m = n+1
  while !isprime(m)
    m += 1
  end
  return m
end

# solution_count(N) = (sigma0(N^2) + 1) / 2
# N has be factored into product of primes already
# Sigma0(N^2) is inlined by doubling the power of each prime
function solution_count(d :: Dict)
  return div(prod([2*v + 1 for v in values(d)]) + 1, 2)
end

# Seach for the least N solving 1/x + 1/y = 1/N with at least the given number of solutions
# Iteratively search using numbers of the form 2^p2 * 3^p3 * 5^p5 ..., where p2 >= p3 >= p5 etc..
# Stop searching once increasing the power on the 2 term doesn't reduce the minimum solution
function least_n_with_num_solutions(numSolutions :: Integer)
  leastN = -1
  p2 = 1
  while true
    n = solution_search(numSolutions, [2 => p2]) 
    if leastN < 0 || n < leastN
      leastN = n
    elseif n > leastN 
      break
    end
    p2 += 1
  end
  return leastN
end

# Workhorse function, searches for value with > numSolutions
# value is kept in factorized form in the Dict d, but is returned as BigInt
function solution_search(numSolutions :: Integer, d :: Dict)

  # base case: D already has enough solutions, so return the value as a BigInt
  if solution_count(d) >= numSolutions
    return prod([BigInt(prime)^power for (prime, power) in d])
  end

  # Recusive case: Find the next prime to add to d, and check with all powers up to the power of the current max prime in d.
  leastN = -1
  maxPrime = maximum(keys(d))
  p = nextprime(maxPrime)
  for exponent = 1 : d[maxPrime]
    d[p] = exponent 
    n = solution_search(numSolutions, d)
    if leastN < 0 || (n > 0 && n < leastN)
      leastN = n
    end     
  end

  # Cleanup the Dict on the way out
  delete!(d, p)
  return leastN
end

using Base.Test

@test solution_count(factor(1260)) == 113
@test least_n_with_num_solutions(113) == 1260
@test least_n_with_num_solutions(1000) == 180180 #from problem 108

end
module problem130

description = """
Composites with prime repunit property
A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.
Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k, for which R(k) is divisible by n, 
  and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.
You are given that for all primes, p > 5, that p − 1 is divisible by A(p). For example, when p = 41, A(41) = 5, and 40 is divisible by 5.
However, there are rare composite values for which this is also true; the first five examples being 91, 259, 451, 481, and 703.

Find the sum of the first twenty-five composite values of n for which GCD(n, 10) = 1 and n − 1 is divisible by A(n).
"""

using problem129

function search(x :: Int)
  results = Int[]
  for n = 2:Inf
    if gcd(n, 10) == 1 && !isprime(n) && (n-1) % problem129.A(n) == 0
      push!(results, n)
      if length(results) == x
        return sum(results)
      end
    end
  end
end

using Base.Test

@test search(5) == sum([91, 259, 451, 481, 703])

end
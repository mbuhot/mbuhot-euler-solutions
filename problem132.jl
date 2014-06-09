module problem132

description = """
Large repunit factors

A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k.
For example, R(10) = 1111111111 = 11×41×271×9091, and the sum of these prime factors is 9414.

Find the sum of the first forty prime factors of R(10^9).
"""

using problem129

# when k divides n, then R(k) divides R(n), which implies that the prime factors of R(k) also divide R(n)
# The function below uses this to find the first Repunit that each prime divides using problem129.A(p)
# It then checks if that k divides the required n.
function search(n = 10^9, facs = 40, maxprime = 200000)
  factors = Int[]
  for p in primes(maxprime)
    if 10 % p == 0 continue end
    k = problem129.A(p)
    if n % k == 0
      push!(factors, p)
      if length(factors) == facs
        return sum(factors)
      end
    end
  end
end

using Base.Test

@test search(10, 4) == sum([11, 41, 271, 9091])

end
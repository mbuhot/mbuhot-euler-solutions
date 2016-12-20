module problem132

description = """
Large repunit factors

A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k.
For example, R(10) = 1111111111 = 11×41×271×9091, and the sum of these prime factors is 9414.

Find the sum of the first forty prime factors of R(10^9).
"""

# Optimized search
# R(n) = (10^n - 1)/9
# R(n) = 0 mod p
# (10^n - 1) / 9 = 0 mod p
# 10^n - 1 = 0 mod 9p
# 10^n = 1 mod 9p
# so search for p satisfying 10^n = 1 mod 9p using Julias powermod function 
function search(n = 10^9, facs = 40, maxprime = 200000)
  factors = Int[]
  for p in primes(maxprime)
    if powermod(10, n, 9*p) == 1
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
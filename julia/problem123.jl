module problem123

description = """
Prime square remainders

Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn−1)^n + (pn+1)^n is divided by pn^2.
For example, when n = 3, p3 = 5, and 4^3 + 6^3 = 280 ≡ 5 mod 25.
The least value of n for which the remainder first exceeds 10^9 is 7037.

Find the least value of n for which the remainder first exceeds 10^10.
"""

# Computes a^b % n
# Definition from Wikipedia on Modular exponentiation: http://en.wikipedia.org/wiki/Modular_exponentiation
# BigInt is required, as a*a will overflow for large a and n
function powmod(a :: BigInt, b :: Integer, n :: Integer)
  x = BigInt(1)
  a = a % n
  while b > 0
    if (b % 2) == 1
      x = (x * a) % n
    end
    b = b >> 1
    a = (a * a) % n
  end
  return x
end

function solve(rmin = 10^10, maxprime = 10^6)
  ps = primes(maxprime)
  for n = 1:length(ps)
    p = BigInt(ps[n])
    psq = p * p
    if psq < rmin
      continue
    end
    r = (powmod(p-1, n, psq) + powmod(p+1, n, psq)) % psq
    if r > rmin
      return n
    end
  end
  error("No solution for rmin=$rmin maxprime=$maxprime")
end

using Base.Test

@test (powmod(BigInt(4), 3, 25) + powmod(BigInt(6), 3, 25)) % 25 == 5
@test solve(10^9) == 7037

end
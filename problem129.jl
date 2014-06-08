module problem129

description = """
Repunit divisibility

A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.
Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k, for which R(k) is divisible by n, 
and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.
The least value of n for which A(n) first exceeds ten is 17.

Find the least value of n for which A(n) first exceeds one-million.
"""

# Calculate repunit length k = (10^k - 1) / 9
function R(k :: Int)
  return div(BigInt(10)^k - 1, 9)
end

# find the least value of k such that R(k) is a multiple of n
function A(n)
  r = BigInt(1)
  assert(gcd(n, 10) == 1)
  for k = 1:Inf
    if r % n == 0
      return k
    end
    r = 10*r + 1 # calculate the next repunit
  end
end

# Search for the least value of n, such that A(n) > x
# The main insight here is that search(x) >= x, so search 1,000,000 doesn't require
#  searching 1..1000000. 
function search(x = 1000000)
  for n = x:Inf
    if gcd(n, 10) == 1
      k = A(n)
      if k > x
        return n
      end
    end
  end
end

using Base.Test

@test R(6) == 111111
@test A(7) == 6
@test A(41) == 5
@test search(10) == 17

end
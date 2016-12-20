module problem120

description = """
Square remainders
Let r be the remainder when (a−1)^n + (a+1)^n is divided by a^2.
For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49. And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.

For 3 ≤ a ≤ 1000, find ∑ rmax.
"""

# compute the maximum value for r = ((a-1)^n + (a+1)^n) % (a^2)
# For increasing values of n, this is a repeating sequence.
# Stop searching for max r when the first value is repeated.
# Perform the power operations using modulo arithmetic to prevent overflow, reusing the results of the previous iterations.
function rmax(a :: Int)
  as1 = a - 1
  ap1 = a + 1
  asq = a * a
  r1 = (as1 + ap1) % asq
  result = r1
  while true
    as1 = (as1 * (a-1)) % asq
    ap1 = (ap1 * (a+1)) % asq
    r = (as1 + ap1) % asq
    if r == r1 
      return result
    end
    result = max(result, r)
  end
end

function sumrmax(low=3, high=1000)
  return sum(map(rmax, low:high))
end

using Base.Test
@test rmax(7) == 42

end
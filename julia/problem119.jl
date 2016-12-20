module problem119

description = """
Digit power sum

The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 83 = 512. Another example of a number with this property is 614656 = 284.
We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.
You are given that a2 = 512 and a10 = 614656.

Find a30.
"""

# sum the digits of an integer by repeated div/mod by 10
function digitsum(n :: Integer)
  total = 0
  while n > 0
    total += n % 10
    n = div(n, 10)
  end
  return total
end

# Find all numbers with are powers of their digit sums, up to a maximum number of digits
# Insight: the digit sum for any number < 10^N can be at most N*9
#          so just consider powers of i from 2 to 9N, checking digitsums
function digitPowerSums(maxDigits = 15)
  results = BigInt[]
  xMax = BigInt(10)^maxDigits
  for i = 2 : 9 * maxDigits
    x = BigInt(i)
    while x < xMax
      if x > 10 && digitsum(x) == i
        push!(results, x)
      end
      x *= i
    end
  end
  sort!(results)
  return results
end


using Base.Test

@test digitsum(1234) == (1+2+3+4)
a = digitPowerSums()
@test a[2] == 512
@test a[10] == 614656

end
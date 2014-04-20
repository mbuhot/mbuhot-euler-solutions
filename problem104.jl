module problem104

description = """
Pandigital Fibonacci ends
Problem 104

The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
"""

# test if the string representation of a number starts with digits 1-9
is_start_pandigital(x :: String) = (length(x) >= 9) && all([in(c, x[1:9]) for c = '1':'9'])


# test if an integer ends with digits 1-9
# This has been optimized to avoid memory allocations as it is the inner loop
function is_end_pandigital(x :: Int, digits=zeros(Bool, 10))
  digits[:] = false
  for i = 1:9
    digits[x % 10  + 1] = true
    x = div(x, 10)
  end
  for i = 2:10
    if !digits[i]
      return false
    end
  end
  return true
end 


# Find the first fibonacci that starts with and ends with digits 1-9
# Calculate fibonacci sequence in BigInts, and in Int64s (modulo 10^10)
# Test for end-pandigital on the native ints, and when found, test the BigInts for start-pandigital
function find_start_end_pandigital()
  a, b = 1, 1
  A, B = BigInt(a), BigInt(b)
  buf = zeros(Bool, 10)
  for k = 3:1000000
    a, b = b, (a+b) % 10000000000
    A, B = B, (A+B)
    if is_end_pandigital(b, buf)
      if is_start_pandigital(string(B))
        return k
      end
    end
  end
end 

using Base.Test

@test is_start_pandigital("3219485766456")
@test !is_start_pandigital("10201049586723")
@test is_end_pandigital(958928534791826)

end
module problem111

description = """
Primes with runs

Considering 4-digit primes containing repeated digits it is clear that they cannot all be the same: 1111 is divisible by 11, 2222 is divisible by 22, and so on. But there are nine 4-digit primes containing three ones:
1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

We shall say that M(n, d) represents the maximum number of repeated digits for an n-digit prime where d is the repeated digit, N(n, d) represents the number of such primes, and S(n, d) represents the sum of these primes.
So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime where one is the repeated digit, there are N(4, 1) = 9 such primes, and the sum of these primes is S(4, 1) = 22275. It turns out that for d = 0, it is only possible to have M(4, 0) = 2 repeated digits, but there are N(4, 0) = 13 such cases.

In the same way we obtain the following results for 4-digit primes.
Digit, d 	M(4, d) 	N(4, d) 	S(4, d)
0 	2 	13 	67061
1 	3 	9 	22275
2 	3 	1 	2221
3 	3 	12 	46214
4 	3 	2 	8888
5 	3 	1 	5557
6 	3 	1 	6661
7 	3 	9 	57863
8 	3 	1 	8887
9 	3 	7 	48073

For d = 0 to 9, the sum of all S(4, d) is 273700.

Find the sum of all S(10, d).
"""

function solve(n :: Integer)
  return sum([S(n, d) for d = 0:9])
end

# search for the first r from (n-1) to 2 producing some primes having the digit d repeat r times in n-digit numbers.
function S(n :: Integer, d :: Integer)
  for r = n-1 : -1 : 2
    result = S(n, d, r)
    if result > 0
      return result
    end
  end
end

# Find the sum of primes with n digits, having digit d repeat r times.
function S(n :: Integer, d :: Integer, r :: Integer)
  total = 0
  repeatCombinations = collect(combinations([1 : (d == 0 ? n-1 : n)], r)) # no leading zeros
  for repeated in repeatCombinations
    digits = zeros(n)
    digits[repeated] = d
    changing = setdiff([1:n], repeated)
    total += SPrimes(digits, changing, 1)
  end
  return total
end

function SPrimes(digits :: Vector, changing :: Vector, i :: Integer)

  # Base case: all digits are set, check if result is prime
  if i > length(changing)
    n = sum([int(10^(x-1) * digits[x]) for x in 1:length(digits)])
    return isprime(n) ? n : 0
  end

  # recursive case, set digit at index changing[i], and call with i+1
  total = 0
  for d = (changing[i] == length(digits) ? 1 : 0) : 9
    digits[changing[i]] = d
    total += SPrimes(digits, changing, i+1)
  end
  return total
end

using Base.Test

@test solve(4) == 273700

end
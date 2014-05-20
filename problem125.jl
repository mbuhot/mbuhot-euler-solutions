module problem125

description = """
Palindromic sums

The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.
There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. 
Note that 1 = 0^2 + 1^2 has not been included as this problem is concerned with the squares of positive integers.
Find the sum of all the numbers less than 10^8 that are both palindromic and can be written as the sum of consecutive squares.
"""

function palendromic(n)
  digits = Int[]
  while n > 0
    push!(digits, n % 10)
    n = div(n, 10)
  end
  return digits == digits[end:-1:1]
end

function solve(n=10^8)
  squares = [(i, i^2) for i=1:int(sqrt(n))]
  k = 1
  special = Int[]
  while length(squares) > 0
    squares = [(i, s + (i+k)^2) for (i, s) in squares]
    squares = filter(x -> x[2] < n, squares)
    for x in squares
      if palendromic(x[2])
        special = union(special, x[2])
      end
    end
    k += 1
  end
  return sum(special)
end

using Base.Test

@test palendromic(595)
@test !palendromic(1234)
@test solve(1000) == 4164

end
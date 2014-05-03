module problem116

description = """
Red, green or blue tiles
A row of five black square tiles is to have a number of its tiles replaced with coloured oblong tiles chosen from red (length two), green (length three), or blue (length four).
If red tiles are chosen there are exactly seven ways this can be done.
If green tiles are chosen there are three ways.
And if blue tiles are chosen there are two ways.
Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the black tiles in a row measuring five units in length.

How many different ways can the black tiles in a row measuring fifty units in length be replaced if colours cannot be mixed and at least one coloured tile must be used?
"""

# Fill function, based on problems 114, 115
function F(m::Integer, n :: Integer, memo = zeros(Int, n))
  # Base case: no space remaining in the row
  if n < m return 0 end

  # Recursive case, count 1 for each placement of block at positions 1:n-m+1, and all ways of
  # filling the remaining space at the end of the row after each placement, memoizing results.
  if memo[n] == 0
    total = 0
    for blockpos = 1:(n-m+1)
      total += 1 + F(m, n - blockpos - m + 1, memo)
    end
    memo[n] = total
  end
  return memo[n]
end

# total ways to fill a row with only red,blue or green tiles.
function homogenous_replacements(n :: Integer)
  return F(2, n) + F(3, n) + F(4, n)
end

using Base.Test

@test F(2, 5) == 7
@test F(3, 5) == 3
@test F(4, 5) == 2
@test homogenous_replacements(5) == (7+3+2)

end
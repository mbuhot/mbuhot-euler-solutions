module problem117

description = """
Red, green, and blue tiles
Using a combination of black square tiles and oblong tiles chosen from: 
 red tiles measuring two units, 
 green tiles measuring three units, 
 and blue tiles measuring four units, 
 it is possible to tile a row measuring five units in length in exactly fifteen different ways.

How many ways can a row measuring fifty units in length be tiled?"""

# Fill function, based on problems 114, 115, 116
function F(n :: Integer, memo = zeros(Int, n))
  # Base case: no space remaining in the row
  if n < 2 return 0 end

  # Recursive case, count 1 for each placement of block at positions 1:n-m+1, and all ways of
  # filling the remaining space at the end of the row after each placement, memoizing results.
  if memo[n] == 0
    total = 0
    for m=2:4, blockpos = 1:(n-m+1)
      total += 1 + F(n - blockpos - m + 1, memo)
    end
    memo[n] = total
  end
  return memo[n]
end

function mixed_fill_count(n :: Integer)
  return 1 + F(n) # +1 for empty row being a valid solution
end


using Base.Test

@test mixed_fill_count(5) == 15

end
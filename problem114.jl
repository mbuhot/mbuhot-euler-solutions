module problem114

description = """
Counting block combinations I
A row measuring seven units in length has red blocks with a minimum length of three units placed on it, 
 such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square. 
There are exactly seventeen ways of doing this.
How many ways can a row measuring fifty units in length be filled?
"""

function block_combinations(n :: Integer, memo = zeros(Int, n))
  # trivial cases
  if n < 1 return 1 end

  # Count the total with each block size, and block position, 
  # recursively counting the ways to fill the remaining space at the end of the row.  
  if memo[n] == 0
    total = 1
    for blocksize = 3:n, blockpos = 1:(n-blocksize+1)
      total += block_combinations(n - blockpos - blocksize, memo)
    end
    memo[n] = total
  end
  return memo[n]
end


using Base.Test

@test block_combinations(3) == 2 #empty or 1 block
@test block_combinations(4) == 4 #empty or length 3 at pos 1, or length 3 at pos 2, or length 4 at pos 1
@test block_combinations(7) == 17

end
module problem115

description = """
Counting block combinations II

A row measuring n units in length has red blocks with a minimum length of m units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square.
Let the fill-count function, F(m, n), represent the number of ways that a row can be filled.
For example, F(3, 29) = 673135 and F(3, 30) = 1089155.
That is, for m = 3, it can be seen that n = 30 is the smallest value for which the fill-count function first exceeds one million.
In the same way, for m = 10, it can be verified that F(10, 56) = 880711 and F(10, 57) = 1148904, so n = 57 is the least value for which the fill-count function first exceeds one million.

For m = 50, find the least value of n for which the fill-count function first exceeds one million.
"""

function F(m::Integer, n :: Integer, memo = zeros(Int, n))
  # trivial cases
  if n < 1 return 1 end

  # Count the total with each block size, and block position, 
  # recursively counting the ways to fill the remaining space at the end of the row.  
  if memo[n] == 0
    total = 1
    for blocksize = m:n, blockpos = 1:(n-blocksize+1)
      total += F(m, n - blockpos - blocksize, memo)
    end
    memo[n] = total
  end
  return memo[n]
end



using Base.Test

@test F(3, 29) == 673135
@test F(3, 30) == 1089155 
@test F(10, 56) == 880711 
@test F(10, 57) == 1148904
@test F(50, 167) == 978181
@test F(50, 168) == 1053389 # <- answer

end
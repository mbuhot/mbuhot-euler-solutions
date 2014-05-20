module problem124

description = """
Ordered radicals
The radical of n, rad(n), is the product of the distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.
Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).
""

# Calculate rad for all values between 1 and n using algorithm similar to sieve of eratosthenes 
function radsieve(n)
  rad = ones(Int, n)
  for i = 2:n 
    if rad[i] == 1
      for j = i:i:n
        rad[j] *= i
      end
    end
  end
  return rad
end

function solve(n=100000, k=10000)
  radsorted = sort(collect(enumerate(radsieve(n))), by = pr -> pr[2], alg=MergeSort)
  return radsorted[k][1]
end

using Base.Test

@test radsieve(10) == [1, 2, 3, 2, 5, 6, 7, 2, 3, 10]
@test solve(10, 4) == 8
@test solve(10, 6) == 9

end
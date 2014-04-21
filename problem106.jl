module problem106

description = """
Special subset sums: meta-testing
Problem 106

Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

    S(B) ≠ S(C); that is, sums of subsets cannot be equal.
    If B contains more elements than C then S(B) > S(C).

For this problem we shall assume that a given set contains n strictly increasing elements and it already satisfies the second rule.

Surprisingly, out of the 25 possible subset pairs that can be obtained from a set for which n = 4, only 1 of these pairs need to be tested for equality (first rule). Similarly, when n = 7, only 70 out of the 966 subset pairs need to be tested.

For n = 12, how many of the 261625 subset pairs that can be obtained need to be tested for equality?

NOTE: This problem is related to problems 103 and 105.
"""

# I have not put any thought into how the solution here can be used to optimize problems 103 and 105
# as the solutions I have to those problems are already pretty fast.

# tests if a sum check would be required, given the indexes into the sorted list of items making two subsets A and B
function checking_required(a :: Vector{Int}, b :: Vector{Int})

  # by the second property of special sets, non-equal subset sizes have different sums
  if length(a) != length(b)
    return false
  end

  # must be disjoint
  if length(intersect(a, b)) > 0
    return false
  end

  # checking is not required if for each item in A, there is a corresponding item in B with a higher index (or vice versa)
  largerA, largerB = 0,0
  sort!(a)
  sort!(b)                        
  for n = length(a):-1:1
    if a[n] > b[n]
      largerA += 1
    else
      largerB += 1
    end
  end
  return (largerA > 0) && (largerB > 0)
end


# total number of checks required for sets of size N
# is number of checks required for each pair of subsets sized from 2 to N/2
function count_checking_required(n)
  total = 0
  for m = 2:floor(n/2)
    cs = collect(combinations([1:n], m))
    for i = 1:length(cs)-1
      for j = i+1:length(cs)
        if checking_required(cs[i], cs[j])
          total += 1
        end
      end
    end
  end
  return total
end


using Base.Test

@test count_checking_required(4) == 1
@test count_checking_required(7) == 70

#println(count_checking_required(12)) 

end
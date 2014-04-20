module problem103

# Special set is a set of values, maintaining the two properties:
# 1) Every disjoint subset has a unique sum
# 2) every subset size N has greater sum than all subsets size < N
# The values member contains the items in the special set
# The sums member tracks the unique sums for all possible subsets
type SpecialSet
  values :: Vector{Int}
  sums :: Vector{Int}
end

# add the value x to SpecialSet s, assumes can_add(x, s) is true
function add(x :: Int, s :: SpecialSet)
  return SpecialSet([x;s.values], [x;s.sums;x+s.sums])
end

# Check if value x can be added to SpecialSet s, maintaining the SpecialSet invariants 
function can_add(x :: Int, s :: SpecialSet)

  # must be a new minimum value
  if x >= s.values[1]
    return false
  end

  # x + any existing sum should be unique
  # implies that the sum of any subset containing x would be unique 
  for y in s.sums
    if in(x+y, s.sums)
      return false
    end
  end

  # new min + old min must be greater than max
  # implies that any subset containing the min will sum to greater than any subset with fewer items 
  if x + s.values[1] <= s.values[end]
    return false
  end

  return true
end

# Generate all SpecialSets having minimum value=xmin, max value=xmax, length=n
function specials(xmin :: Int, xmax :: Int, n :: Int)

  # base case: all length 2 sets are SpecialSets
  if n == 2
    return [SpecialSet([xmin, xmax], [xmin, xmax, xmin+xmax])]
  end

  # recursive case: Find all special sets from mid to max, length n-1
  # Then check if xmin can be added to the specialset
  results = SpecialSet[]
  mid = max(xmin + 1, xmax - xmin + 1) 
  for x = mid : xmax-1
    for s in specials(x, xmax, n-1)
      if can_add(xmin, s)
        push!(results, add(xmin, s))
      end
    end
  end
  
  return results
end

# returns the values vector of the SpecialSet with minimum sum
# having min, max and length specified
function optimum_special_set(xmin :: Int, xmax :: Int, n :: Int)
  sets = specials(xmin, xmax, n)
  totals = [sum(s.values) for s in sets]
  t, i = findmin(totals)
  return sets[i].values
end

using Base.Test

@test optimum_special_set(3, 7, 4) == [3, 5, 6, 7]
@test optimum_special_set(6, 13, 5) == [6, 9, 11, 12, 13]
@test optimum_special_set(11, 25, 6) == [11, 18, 19, 20, 22, 25]

# based on the hints in the question, the bounds of the solution should be 20 and 45
println(optimum_special_set(20, 45, 7)')
	
end
module problem118

description = """
Pandigital prime sets
Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, different sets can be formed. 
Interestingly with the set {2,5,47,89,631}, all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?
"""

# Convert an array of digits to an integer
function digitsToInt(digits :: Array)
  n = 0
  for d in digits
    n = n*10 + d
  end
  return n
end

# calculate the number of permutations of q that are prime
# Stores results in memo, for faster lookup for the same digits in future calls
function primePermutations(q :: Vector, memo :: Dict)
  total = 0
  sort!(q)
  key = digitsToInt(q)
  if haskey(memo, key)
    return memo[key]
  end

  for p in permutations(q)
    if isprime(digitsToInt(p))
      total += 1
    end
  end
  memo[key] = total
  return total
end

# Calculate the number of sets containing permutations of digits 1-9 that are all prime
# Julia's built in partitions, permutations and isprime do all the work :)
# For a given partition of [1:9] the number of sets is the product of prime permutations of each sub-set of digits.
function run()
  total = 0
  memo = (Int=>Int)[]
  for p in partitions([1:9])
    total += prod([primePermutations(q, memo) for q in p])
  end
  return total
end

end
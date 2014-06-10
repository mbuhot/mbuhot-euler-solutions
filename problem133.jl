module problem133

description = """
Repunit nonfactors

A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.
Let us consider repunits of the form R(10^n).
Although R(10), R(100), or R(1000) are not divisible by 17, R(10000) is divisible by 17. 
Yet there is no value of n for which R(10^n) will divide by 19. 
In fact, it is remarkable that 11, 17, 41, and 73 are the only four primes below one-hundred that can be a factor of R(10n).

Find the sum of all the primes below one-hundred thousand that will never be a factor of R(10^n).
"""

# Search the list of primes, for each one either:
# 1) 10^10^n = 1 mod 9p for some n, which means p divides R(10^n)
# 2) A cycle forms in the remainders of 10^10^n mod 9p
# So search the list of primes until a 1 occurs in the remainder or a repeated value is hit.
# IntSet does a pretty good job providing a constant time test for checking if a value has already been seen.
function search(maxprime = 100000)
  total = 0
  for p in primes(maxprime)
    seen = IntSet()
    remainder = (10^10) % (9*p)
    push!(seen, remainder)
    for n = 2:Inf  
      remainder = powermod(remainder, 10, 9*p)
      if remainder == 1
        break
      elseif in(remainder, seen)
        total += p
        break
      end 
      push!(seen, remainder)
    end
  end
  return total
end

using Base.Test

@test search(100) == sum(primes(100)) - sum([11, 17, 41, 73])

end
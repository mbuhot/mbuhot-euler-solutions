module problem108

description = """
Diophantine reciprocals I
Problem 108

In the following equation x, y, and n are positive integers.
1/x + 1/y = 1/n

For n = 4 there are exactly three distinct solutions:
1/5 + 1/20 = 1/4
1/6 + 1/12 = 1/4
1/8 + 1/8 = 1/4

What is the least value of n for which the number of distinct solutions exceeds one-thousand?

NOTE: This problem is an easier version of problem 110; it is strongly advised that you solve this one first.
"""


# Brute force check for 1/y + 1/x = 1/n for x in the range n+1 to 2n
# Integer y exists when (x-n) divides x*n, so no need to actually calulate the fractions.
function solutionCount(n :: Int)
  c = 0
  xn = n*(n+1)
  xmn = 1
  for x = n+1 : n * 2
    if xn % xmn == 0
      c += 1
    end
    xn += n
    xmn += 1
  end
  return c
end

   
using Base.Test

@test solutionCount(4) == 3

# all solutions take the form:
# a/(n*k) + (k-a)/(n*k) = 1/n, 
# where a is a factor of n*k, and (k-a) is a factor of n*k
# I arrived at this solution by trial and error playing with the solutionCount above.
# Originally, I had only considered the case where a=1, reducing the problem to N having >1000 divisors.
# The solution to that problem requires a large value for Sigma0(n) which implies any prime factors.
@test solutionCount(2*2*3*3*5*7*11*13) > 1000

end

module problem113

description = """
Non-bouncy numbers

Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
As n increases, the proportion of bouncy numbers below n increases such that there are only 12951 numbers below one-million that are not bouncy and only 277032 non-bouncy numbers below 10^10.

How many numbers below a googol (10^100) are not bouncy?
"""

# Count the number of non-bouncy numbers having a given number of digits
# This is sufficent to solve the problem of non-bouncy's less than 10^100, numDigits = 100
# Non-bouncy count is increasing + decreasing - flat (eg, 111, 222, 333)
function non_bouncy_count(numdigits :: Integer)
  return increasing(numdigits) + decreasing(numdigits) - 9*numdigits
end

# count of increasing numbers with maximum number of digits
# Solve this by tabulating numdigits vs maxDigit in number, table[3, 7] is number of 3-digit increasing numbers having max digit=7
# A pattern appears where i,j = i-1,j + i,j-1
# First row and first column are all 1's 
function increasing(numDigits :: Integer)
  table = zeros(Int, numDigits, 9)
  table[1,:] = 1
  table[:,1] = 1
  for i = 2:numDigits
    for j = 2:9
      table[i,j] = table[i-1, j] + table[i, j-1]
    end
  end
  return sum(table)
end

# Similar to increasing, tabulate the solution, but requires some care because 0 can appear in a decreasing number,
# but zero is not counted as a single digit decreasing number.
# In this function, table[4, 8] is number of 4-digit increasing numbers with min digit = 9 (offset by 1 to accomodate 0)
function decreasing(numDigits :: Integer)
  table = zeros(Int, numDigits, 10)
  table[1, :] = 1
  table[1, 1] = 0 # zero is not counted 
  table[:,10] = 1
  for i = 2:numDigits
    for j = 9:-1:1
      table[i, j] = table[i-1, j] + table[i, j+1]
    end
  end
  return sum(table) 
end

using Base.Test
@test increasing(1) == 9
@test increasing(2) == 45 + 9
@test decreasing(1) == 9
@test decreasing(2) == 54 + 9
@test non_bouncy_count(6) == 12951
@test non_bouncy_count(10) == 277032 

end
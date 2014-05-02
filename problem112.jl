module problem112

description = """
Bouncy numbers

Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""

function increasing(n :: Integer)
  lastDigit = 9
  while n > 0
    d = n % 10
    if d > lastDigit
      return false
    end
    lastDigit = d; 
    n = div(n, 10)
  end
  return true  
end

function decreasing(n :: Integer)
  lastDigit = 0
  while n > 0
    d = n % 10
    if d < lastDigit
      return false
    end
    lastDigit = d; 
    n = div(n, 10)
  end
  return true
end

function bouncy(n :: Integer)
  return !(increasing(n) || decreasing(n))
end

function bouncySearch(percentage :: Integer)
  n = 1
  b = 0
  while b*100 != n*percentage
    n += 1
    b += bouncy(n) ? 1 : 0
  end
  return n
end

using Base.Test

@test bouncySearch(90) == 21780

end
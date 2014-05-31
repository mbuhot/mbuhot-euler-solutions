module problem127

description = """
abc-hits
The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:
GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
a < b
a + b = c
rad(abc) < c

For example, (5, 27, 32) is an abc-hit, because:
GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
5 < 27
5 + 27 = 32
rad(4320) = 30 < 32

It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c < 1000, with ∑c = 12523.
Find ∑c for c < 120000.
"""

# calculate rad(x) for x=1:n using prime sieve 
function radsieve(n :: Int)
  r = ones(Int, n)   
  for i = 2:n
    if r[i] == 1     
      for j = i:i:n
        r[j] *= i
      end
    end
  end
  return r
end

# Calculate sum(c) for c < cmax and a,b,c is an ABC-Hit
function abchits(cmax :: Int = 120000)
  # Pre-compute rad, and sort 1:cmax by rad
  r = radsieve(cmax)
  p = sortperm(r)

  csum = 0
  for c = 3:cmax
    radc = r[c]

    # rad(a*b*c) == rad(a) * rad(b) * rad(c) when a,b,c are coprime
    # rad(a)*rad(b)*rad(c) < c implies rad(a) < c / (rad(c) * rad(b))
    # using 2 as a lower bound for rad(b), max value for rad(a) is c / (2 * rad(c))
    radamax = div(c, radc * 2)
    amax = div(c, 2)

    # search the sorted list for suitable rad(a), a
    for i = 1:cmax
      a = p[i]
      rada = r[a]
      if rada > radamax break end # stop searching once rad(a) is too large
      if a  > amax continue end   # skip over a that are too large
      b = c - a
      radb = r[b]

      # gcd(a,c) == 1 implies gcd(a,b) == 1 and gcd(b,c) == 1
      # if there were some d that divides a and b, then d would also divide (a+b)
      if rada * radb * radc < c && gcd(a, c) == 1 
        csum += c
      end
    end
  end

  return csum
end
	
end
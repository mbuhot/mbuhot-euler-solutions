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

function abchits(cmax :: Int)
  r = radsieve(cmax)
  s = sort(collect(enumerate(r)), by=x->x[2], alg=MergeSort)	

  for c = 3:cmax
    radc = r[c]
    radamax = div(c, radc * 2)
    amax = div(c, 2)
    for (a, rada) in s
      if rada > radamax break end
      if a  > amax continue end
      b = c - a
      radb = r[b]
      if rada * radb * radc < c &&
         gcd(a, c) == 1 &&
         gcd(a, c) == 1 && 
         gcd(b, c) == 1
        produce((a,b,c))
      end
    end
  end
end

function abchitcsum(cmax :: Int)
  total = 0
  for (a,b,c) in @task abchits(cmax)
    total += c
  end
  return total
end

end
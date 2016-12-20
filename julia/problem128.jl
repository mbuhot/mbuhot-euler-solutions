module problem128
  
description = """
Hexagonal tile differences

A hexagonal tile with number 1 is surrounded by a ring of six hexagonal tiles, starting at "12 o'clock" and numbering the tiles 2 to 7 in an anti-clockwise direction.
New rings are added in the same fashion, with the next rings being numbered 8 to 19, 20 to 37, 38 to 61, and so on. The diagram below shows the first three rings.
By finding the difference between tile n and each its six neighbours we shall define PD(n) to be the number of those differences which are prime.
For example, working clockwise around tile 8 the differences are 12, 29, 11, 6, 1, and 13. So PD(8) = 3.
In the same way, the differences around tile 17 are 1, 17, 16, 1, 11, and 10, hence PD(17) = 2.
It can be shown that the maximum value of PD(n) is 3.

If all of the tiles for which PD(n) = 3 are listed in ascending order to form a sequence, the 10th tile would be 271.
Find the 2000th tile in this sequence.
"""

# Value at the top of each ring is calculated using arithmetic series
# a = First element, d = common difference, n = num terms to sum
arithmetic_series(a, d, n) = div((2*a + (n-1)*d)*n,2)

# The value at the start of each ring
ringstart(ring :: Int) = ring == 1 ? 1 : 2 + arithmetic_series(0, 6, ring-1)

# The value at the start of one side in a ring
sidestart(ring :: Int, side :: Int) = ringstart(ring) + (side-1) * (ring-1)

# The value at a given ring, side and position along the side
valueat(ring :: Int, side :: Int, pos :: Int) = sidestart(ring, side) + (pos-1)

# Calculates the neighbours of a given tile, given by its ring, side and position
# Special care required at side=1,pos=1 and side=6,pos=ring-1
# There are always 2 tiles adjacent in the same ring
# When pos = 1, there are 3 adjacent on the next ring, and 1 on the previous
# otherwise, there are 2 adjacent on the next ring, and 2 on the previous
function neighbours(ring :: Int, side :: Int, pos :: Int)
  a = valueat(ring, side, pos)
  b = (side == 1 && pos == 1) ? valueat(ring, 6, ring-1) : (a-1) 
  c = (side == 6 && pos == (ring-1)) ? valueat(ring, 1, 1) : (a+1) 
  d = (side == 6 && pos == (ring-1)) ? valueat(ring-1, 1, 1) : valueat(ring-1, side, pos)
  if pos == 1
    e = valueat(ring+1, side, pos) 
    f = valueat(ring+1, side, pos+1)
    g = valueat(ring+1, side == 1 ? 6 : side-1, ring)
  else
    e = valueat(ring-1, side, pos-1)
    f = valueat(ring+1, side, pos)
    g = valueat(ring+1, side, pos+1)
  end
  return [b,c,d,e,f,g]
end

# search for the N'th value having 3 adjacent tiles with prime difference
# Testing found that these only occur at side=1, pos=1 and side=6, pos=ring-1
function search(N=2000)
  found = 1 # 1 is a 3 prime diff with 3,4,6
  for ring = 2:Inf, (side, pos) in [(1, 1), (6, ring-1)]
    v = valueat(ring, side, pos)
    n = neighbours(ring, side, pos)
    diffs = abs(n - v)
    if count(isprime, diffs) == 3
      found += 1 
    end
    if found == N
      return v
    end
  end 
end

using Base.Test

@test ringstart(1) == 1
@test ringstart(2) == 2
@test ringstart(3) == 8
@test ringstart(4) == 20
@test sidestart(2, 1) == 2
@test sidestart(2, 3) == 4
@test sidestart(4, 6) == 35
@test valueat(4, 1, 1) == 20
@test valueat(4, 6, 3) == 37
@test sort(neighbours(2, 1, 1)) == [1, 3, 7, 8, 9, 19]
@test sort(neighbours(3, 2, 2)) == [3, 4, 10, 12, 24, 25]
@test sort(neighbours(3, 6, 2)) == [2, 7, 8, 18, 36, 37]
@test search(10) == 271
end
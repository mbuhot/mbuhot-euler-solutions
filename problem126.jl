module problem126

export Cuboid

description = """
Cuboid layers

The minimum number of cubes to cover every visible face on a cuboid measuring 3 x 2 x 1 is twenty-two.
If we then add a second layer to this solid it would require forty-six cubes to cover every visible face, 
the third layer would require seventy-eight cubes, and the fourth layer would require one-hundred and eighteen cubes to cover every visible face.

However, the first layer on a cuboid measuring 5 x 1 x 1 also requires twenty-two cubes; 
similarly the first layer on cuboids measuring 5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain forty-six cubes.

We shall define C(n) to represent the number of cuboids that contain n cubes in one of its layers. 
So C(22) = 2, C(46) = 4, C(78) = 5, and C(118) = 8.
It turns out that 154 is the least value of n for which C(n) = 10.

Find the least value of n for which C(n) = 1000.
"""

# A cube with length, width and height
immutable Cuboid
  l :: Int
  w :: Int
  h :: Int
end

# calculates the middle section of the n'th layer
# equal to (the perimeter of original cube + diagonals) * height or original cube
middle(c :: Cuboid, n :: Int) = (2 * (c.l + c.w) + 4 * (n - 1)) * c.h

# Recurrance relation for calculating the top section of the n'th layer 
# For n = 1, just the area of the top of original cube
# otherwise, equal to the top of the previous layer + a one cube thick rim from the middle of previous layer
top(c :: Cuboid, n :: Int) = 
  if (n == 1) 
    return (c.l * c.w) 
  else 
    return (top(c, n-1) + div(middle(c, n-1), c.h)) 
  end 

# Calculate the n'th layer, top and bottom are symetric + middle section
layer(c :: Cuboid, n :: Int) = 2 * top(c, n) + middle(c, n)

# Calculate the size of all layers of cuboid up to a maximum
# re-uses the results of previous iterations to efficiently calculate the next
function layers(c :: Cuboid, maxsize :: Int)
  n = 1
  t = top(c, n)
  m = middle(c, n)
  x = 0
  result = Int[]
  while true
    x = 2 * t + m
    if x > maxsize break end
    push!(result, x)
    t = t + div(m, c.h)
    n += 1
    m = middle(c, n)
  end
  return result
end

# Search for a solution x, to C(x) == N, for x in 1:guess
# The lower bound is given by layer 1 of cuboid (Length, 1, 1) 
# Once a solution is found < lower bound, search can stop
function search(N :: Int, guess :: Int)
  counts = zeros(Int, guess)
  l = 1
  lowerbound = layer(Cuboid(l, 1, 1), 1) 
  while lowerbound <= guess
    for i = 1:lowerbound-1
      if counts[i] == N
        return i
      end
    end
    w = 1
    while w <= l && layer(Cuboid(l, w, 1), 1) <= guess
      h = 1
      while h <= w && layer(Cuboid(l, w, h), 1) <= guess
        sizes = layers(Cuboid(l,w,h), guess)
        counts[sizes] += 1
        h += 1
      end
      w += 1
    end
    l += 1
    lowerbound = layer(Cuboid(l, 1, 1), 1)
  end
  println("no solution found < $guess")
  return -1
end

using Base.Test

@test layer(Cuboid(3, 2, 1), 1) == 22
@test layer(Cuboid(3, 2, 1), 2) == 46
@test layer(Cuboid(3, 2, 1), 3) == 78
@test layer(Cuboid(3, 2, 1), 4) == 118
@test layer(Cuboid(5, 1, 1), 1) == 22
@test layer(Cuboid(5, 3, 1), 1) == 46
@test layer(Cuboid(7, 2, 1), 1) == 46
@test layer(Cuboid(11, 1, 1), 1) == 46
@test layers(Cuboid(3,2,1), 78) == [22, 46, 78] 
@test search(10, 200) == 154

end
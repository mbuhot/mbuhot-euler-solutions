module problem122

description = """
Efficient exponentiation

The most naive way of computing n15 requires fourteen multiplications:
n × n × ... × n = n15

But using a "binary" method you can compute it in six multiplications:

n × n = n^2
n^2 × n^2 = n^4
n^4 × n^4 = n^8
n^8 × n^4 = n^12
n^12 × n^2 = n^14
n^14 × n = n^15

However it is yet possible to compute it in only five multiplications:

n × n = n^2
n^2 × n = n^3
n^3 × n^3 = n^6
n^6 × n^6 = n^12
n^12 × n^3 = n^15

We shall define m(k) to be the minimum number of multiplications to compute nk; for example m(15) = 5.
For 1 ≤ k ≤ 200, find ∑ m(k).
"""

# Calculates the minimum number of multiplications to compute n^k
# given the known powers, and a maximum cutoff
function muls(k :: Int, known = [1], maxp = k-1)
  if (k % 2) == 0
    return muls(div(k,2)) + 1 # for even powers, solution is always to square the half power
  
  elseif known[end] == k 
    return length(known)-1  # solution found
  
  elseif length(known) >= maxp # no solution for given known path
    return -1
  
  elseif (maxp - length(known)) < floor(log2(k / known[end])) # no possible solution for given knowns
    return -1
  end

  # search for solutions by summing items in the knowns path
  for i = length(known):-1:1
    for j = i:-1:1
      n = known[i] + known[j]
      if n <= k && n > known[end]
        push!(known, n)
        result = muls(k, known, maxp)
        pop!(known)
        if result == -1
          break 
        elseif result == length(known)
          return result
        elseif result < maxp
          maxp = result
        end
      end
    end
  end

  return maxp
end

function solve(maxk = 200)
  total = 0
  for i = 1:maxk
    total += muls(i)
  end
  return total
end

end
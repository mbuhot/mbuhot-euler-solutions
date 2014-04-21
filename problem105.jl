module problem105

using problem103

description = """
Special subset sums: testing
Problem 105

Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

    S(B) ≠ S(C); that is, sums of subsets cannot be equal.
    If B contains more elements than C then S(B) > S(C).

For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because 65 + 87 + 88 = 75 + 81 + 84, whereas {157, 150, 164, 119, 79, 159, 161, 139, 158} satisfies both rules for all possible subset pair combinations and S(A) = 1286.

Using sets.txt (right click and "Save Link/Target As..."), a 4K text file with one-hundred sets containing seven to twelve elements (the two examples given above are the first two sets in the file), identify all the special sum sets, A1, A2, ..., Ak, and find the value of S(A1) + S(A2) + ... + S(Ak).

NOTE: This problem is related to problems 103 and 106.
"""

function sum_of_special_sets()
  total = 0
  sets = read_sets()
  for s in sets
    if is_special_set(s)
      total += sum(s)
    end
  end
  return total
end

function read_sets()
  return map(s -> int(split(s, ',')), open(readlines, "sets.txt"))
end

function is_special_set(s :: Vector{Int})
  sort!(s)
  sp = SpecialSet(s[end-1:end], [s[end], s[end-1], s[end]+s[end-1]])
  for x in s[end-2:-1:1]
    if can_add(x, sp)
      sp = add(x, sp)
    else
      return false
    end
  end
  return true
end

using Base.Test

@test is_special_set([157, 150, 164, 119, 79, 159, 161, 139, 158])
@test !is_special_set([81, 88, 75, 42, 87, 84, 86, 65])

end
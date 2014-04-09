#! /usr/bin/env python3

description = '''
Right triangles with integer coordinates
Problem 91
The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.


There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2.


Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
'''

def rightTriangles(N):
  # To count each triangle only once, require: y2 - x2 < y1 - x1
  count = 0
  for x1 in range(0, N + 1):
    for y1 in range(0 if x1 > 0 else 1, N + 1):
      for x2 in range(0, N + 1):
        for y2 in range(0 if x2 > 0 else 1, y1 - x1 + x2):
          Asq = (x2 - x1)**2 + (y2 - y1)**2
          Bsq = x1**2 + y1**2
          Csq = x2**2 + y2**2
          hyp = max(Asq, Bsq, Csq)
          if Asq>0 and (Asq + Bsq + Csq - hyp) == hyp:
            count += 1
  return count
        
print(rightTriangles(2))
print(rightTriangles(50))

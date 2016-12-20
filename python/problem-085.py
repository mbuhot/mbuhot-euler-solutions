#! /usr/bin/env python3

description = '''
Counting rectangles
Problem 85
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
'''

def subRectangles(subW, subH, outerW, outerH):
  return (outerW - subW + 1) * (outerH - subH + 1)

def numRectangles(w, h):
  return sum(subRectangles(subW, subH, w, h) for subW in range(1, w+1) for subH in range(1, h+1))

assert(18 == numRectangles(2, 3))

best = (1, 1, 1)
for w in range(1, 100):
  for h in range(w, 100):
    score = numRectangles(w, h)
    if abs(2000000 - score) < abs(2000000 - best[0]):
      best = (score, w, h)
      print(best)

print(best[1] * best[2])

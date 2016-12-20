#! /usr/bin/env python3

import itertools

with open('names.txt', 'r') as f:
  names = sorted([n[1:-1] for n in f.readline().split(',')])
assert(names[937] == 'COLIN')

namesums = (sum(ord(c) - ord('A') + 1 for c in n) for n in names)
scores = [s * i for (s,i) in zip(namesums, itertools.count(1))]
assert(scores[937] == 49714)

print('total scores:', sum(scores))


#! /usr/bin/env python3

from collections import defaultdict
from itertools import combinations, permutations, count
from math import sqrt

description = '''
Anagramic squares
Problem 98
By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
'''
def encodes(encoding, word, expected):
  return all(encoding[c] == expected[i] for (i,c) in enumerate(word))
  

def squares(n):
  for i in count(1):
    sqstr = str(i*i)
    if len(sqstr) < n: continue
    elif len(sqstr) > n: break
    else: yield sqstr

def squareEncodings(letters, word1, word2):
  for sq1str in squares(len(word1)):
    c2d = dict(zip(word1, sq1str))
    d2c = dict(zip(sq1str, word1))

    if not encodes(c2d, word1, sq1str): continue
    if not encodes(d2c, sq1str, word1): continue

    for sq2str in squares(len(word1)):
      if encodes(c2d, word2, sq2str):
        yield (c2d, int(sq1str), int(sq2str))

def squareAnagrams(anagrams):
  for (letters, wordset) in anagrams.items():
    print(wordset)
    for (word1, word2) in combinations(wordset, 2):
      for (encoding, n1, n2) in squareEncodings(letters, word1, word2):
        yield(word1, word2, encoding, n1, n2)
            
def readAnagrams():
  with open('words-98.txt', 'r') as f:
    words = [w[1:-1] for w in f.read().split(',')]
  anagrams = defaultdict(set)
  for word in words:
    key = ''.join(sorted(word))
    anagrams[key].add(word)
  return dict((k,v) for (k,v) in anagrams.items() if len(v) > 1)

anagrams = readAnagrams()
results = squareAnagrams(anagrams)
print(max(results, key=lambda x: max(x[3], x[4])))

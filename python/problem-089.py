#! /usr/bin/env python3

description = '''
Roman numerals
Problem 89
The rules for writing Roman numerals allow for many ways of writing each number (see About Roman Numerals...). However, there is always a "best" way of writing a particular number.

For example, the following represent all of the legitimate ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

The last example being considered the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; that is, they are arranged in descending units and obey the subtractive pair rule (see About Roman Numerals... for the definitive rules for this problem).

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
'''

# roman ::= SubtractiveGroup+
# subtractiveGroup ::= D1*D2+ where D1 < D2

digitValues = {
  'I' : 1,
  'V' : 5,
  'X' : 10,
  'L' : 50,
  'C' : 100,
  'D' : 500,
  'M' : 1000
}

def addUnits(s):
  total = 0
  i = 0
  while i < len(s) and s[i] == s[0]: 
    total += digitValues[s[i]]
    i += 1
  return (total, i)

def parseSubtractiveGroup(s):
  total1, i = addUnits(s)
  if i == len(s) or digitValues[s[i]] < digitValues[s[0]]: 
    return (total1, s[i:])
  total2, j = addUnits(s[i:])
  return (total2 - total1, s[i+j:]) 

def parseRoman(s):
  total = 0
  while len(s) > 0:
    v, s = parseSubtractiveGroup(s)
    total += v
  return total

def printRoman(n):
  def gen(n):
    while n > 0:
      sn = str(n)
      if n >= 1000: yield 'M';  n -= 1000
      elif sn[0] not in ['4', '9']:
        if n >= 500: yield 'D'; n -= 500
        elif n >= 100: yield 'C'; n -= 100
        elif n >= 50: yield 'L';  n -= 50
        elif n >= 10: yield 'X';  n -= 10
        elif n >= 5: yield 'V';   n -= 5
        else: yield 'I';          n -= 1
      else:
         if n >= 100: yield 'C';  n += 100
         elif n >= 10: yield 'X'; n += 10
         else: yield 'I';         n += 1
  return ''.join(gen(n))

with open('roman.txt', 'r') as f:
  numerals = [line.strip() for line in f]

saved = 0
for n in numerals:
  m = parseRoman(n)
  s = printRoman(m)
  saved += (len(n) - len(s))

print('characters saved:', saved)


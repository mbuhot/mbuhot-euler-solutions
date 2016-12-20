#! /usr/bin/env python3

description = """
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

_say = {
  1 : 'one',
  2 : 'two',
  3 : 'three', 
  4 : 'four',
  5 : 'five',
  6 : 'six', 
  7 : 'seven',
  8 : 'eight',
  9 : 'nine',
  10: 'ten',
  11 : 'eleven',
  12 : 'twelve',
  13 : 'thirteen',
  14 : 'fourteen',
  15 : 'fifteen',
  16 : 'sixteen',
  17 : 'seventeen',
  18 : 'eighteen',
  19 : 'nineteen', 
  20 : 'twenty',
  30 : 'thirty',
  40 : 'forty',
  50 : 'fifty',
  60 : 'sixty',
  70 : 'seventy',
  80 : 'eighty',
  90 : 'ninety',
}
  
def say(n):
  if n < 100:
    if n in _say: return _say[n]
    tens = (n // 10) * 10
    ones = n % 10
    return '%s %s' % (_say[tens], _say[ones])
  elif n < 1000:
    hundreds = (n // 100)
    rest = n % 100
    if rest == 0:
      return '%s hundred' % say(hundreds)
    else:
      return '%s hundred and %s' % (say(hundreds), say(rest))
  elif n < 1000000:
    thousands = (n // 1000)
    rest = n % 1000
    if rest == 0:
      return '%s thousand' % say(thousands)
    else:
      return '%s thousand %s' % (say(thousands), say(rest))

  
assert(say(11) == 'eleven')
assert(say(95) == 'ninety five')
assert(say(111) == 'one hundred and eleven')
assert(say(592) == 'five hundred and ninety two')
assert(say(111111) == 'one hundred and eleven thousand one hundred and eleven')

print(sum(len(say(n).replace(' ', '')) for n in range(1, 1001)))

#! /usr/bin/env python3

description ="""
Counting Sundays
Problem 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def dayOfWeek(year, month, day):
  """Zellers congruence"""
  date = '%d-%d-%d' % (year, month, day)
  if month <= 2:
    month += 12
    year -= 1
  q = day
  m = month
  k = year % 100
  j = year // 100
  h = (q + ((13 * (m + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7
  return h

assert(dayOfWeek(1900, 1, 1) == 2)
assert(dayOfWeek(2014, 2, 24) == 2)
assert(dayOfWeek(2013, 9, 1) == 1)

daysOfFirst = (dayOfWeek(year, month, 1) for year in range(1901, 2001) for month in range(1, 13))
firstSundays = sum((1 for x in daysOfFirst if x == 1))
print('There are', firstSundays, ' months having sunday on the 1st of the month between 1901 and 2000')


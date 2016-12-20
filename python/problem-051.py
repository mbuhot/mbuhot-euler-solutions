#! /usr/bin/env python3

from prime import isPrime, primes

description = '''
Prime digit replacements
Problem 51
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
'''

def replaceDigits(source, original, replacement):
  return int(source[:-1].replace(str(original), str(replacement)) + source[-1])

def primeDigitReplacements(p, d):
  for j in range(d, 10):
    x = replaceDigits(p, d, j)
    if isPrime(x):
      yield x

def eightPrimeFamilies():
  for p in primes():
    pstr = str(p)
    if   '0' in pstr[:-1]: d = 0
    elif '1' in pstr[:-1]: d = 1
    elif '2' in pstr[:-1]: d = 2
    else: continue
    family = list(primeDigitReplacements(pstr, d))
    if len(family) == 8:
      yield (p, family)    
  
print(next(eightPrimeFamilies())) 

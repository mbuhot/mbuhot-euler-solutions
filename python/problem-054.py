#! /usr/bin/env python3

from collections import defaultdict

description = '''
Poker hands
Problem 54
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 		 Player 2	 		     Winner
1	 	5H 5C 6S 7S KD: Pair of Fives    2C 3S 8S 8D TD: Pair of Eights      Player 2
2	 	5D 8C 9S JS AC: Highest card Ace 2C 5C 7D 8S QH: Highest card Queen  Player 1
3	 	2D 9C AS AH AC: Three Aces       3D 6D 7D TD QD: Flush with Diamonds Player 2
4	 	4D 6S 9H QH QC: Pair of Queens   3D 6D 7H QD QS: Pair of Queens
                             Highest card Nine                   Highest card Seven  Player 1
5	 	2H 2D 4C 4D 4S: Full House       3C 3D 3S 9S 9D: Full House
                              With Three Fours	 		 with Three Threes   Player 1

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''


def cardvalue(card):
  return "23456789TJQKA".index(card[0]) + 2

def suit(card):
  return card[-1]

def highcard(hand1, hand2):
  s1 = sorted(map(cardvalue, hand1), reverse=True)
  s2 = sorted(map(cardvalue, hand2), reverse=True)
  return 1 if s1 > s2 else 2

assert(highcard(['5H', 'QD', '2S', 'AC', '8C'], ['9H', 'KS', '7C', '4S', '3C']) == 1)	


def flush(hand):
  return max(map(cardvalue, hand)) if len(set(map(suit, hand))) == 1 else -1

assert(flush(['5C', '7C', '8C', '2C', 'JC']) == 11)
assert(flush(['5C', '5S', '5H', 'QC', 'AH']) < 0)


def straight(hand): 
  s = sorted(map(cardvalue, hand))
  return s[-1] if all(s[i] == s[i-1] + 1 for i in range(1, 5)) else -1

assert(straight(['5H', '6C', '3D', '4C', '7S']) == 7)
assert(straight(['5H', '6C', '3D', '4C', '8S']) < 0) 


def straightflush(hand):
  fval = flush(hand)
  sval = straight(hand)
  return sval if fval > 0 else fval

assert(straightflush(['5H', '6H', '9H', '7H', '8H']) == 9)
assert(straightflush(['5H', '6H', '9H', '7H', '8C']) < 0) 

def royalflush(hand):
  val = straightflush(hand)
  return -1 if val < cardvalue('AH') else val

assert(royalflush(['KC', 'TC', 'JC', 'QC', 'AC']) > 0)
assert(royalflush(['4C', '6C', '8C', '9C', 'AC']) < 0)

def group(hand):
  d = defaultdict(int)
  for card in map(cardvalue, hand):
    d[card] = d[card] + 1
  return d
  
def fourOfAKind(hand):
  d = group(hand)
  for k,v in d.items():
    if v == 4: return k
  return -1

assert(fourOfAKind(['5C', '5S', '3C', '5H', '5D']) == 5)
assert(fourOfAKind(['4C', '5C', '3C', 'AH', '6S']) < 0) 

def fullhouse(hand):
  d = group(hand)
  s = sorted(d.items(), key=lambda pr: pr[1])
  if len(s) == 2 and s[1][1] == 3:
    return s[1][0]
  return -1

assert(fullhouse(['5C', '5S', '5H', 'AC', 'AH']) == 5)
assert(fullhouse(['5C', '5S', '5H', 'QC', 'AH']) < 0)

def threeOfAKind(hand): 
  d = group(hand)
  for k,v in d.items():
    if v == 3: return k
  return -1

assert(threeOfAKind(['4H', '7S', '7D', '7C', '3H']) == 7)
assert(threeOfAKind(['4H', '6S', '7D', '7C', '3H']) < 0)

def twoPair(hand):
  d = group(hand)
  if sorted(d.values()) == [1,2,2]:
    return max(k for (k,v) in d.items() if v == 2)
  return -1

assert(twoPair(['4H', '5S', '7D', '7C', '4H']) == 7)
assert(twoPair(['4H', '6S', '7D', '7C', '3H']) < 0)

def onePair(hand):
  d = group(hand) 
  for k,v in d.items():
    if v == 2: return k
  return -1

assert(onePair(['4H', '6S', '7D', '7C', '3H']) == 7)
assert(onePair(['4H', '6S', 'AD', '7C', '3H']) < 0)

def rank(hand):
  val = royalflush(hand)
  if val > 0: return (10, val)
  val = straightflush(hand)
  if val > 0: return (9, val)
  val = fourOfAKind(hand)
  if val > 0: return (8, val)
  val = fullhouse(hand)
  if val > 0: return (7, val)
  val = flush(hand)
  if val > 0: return (6, val)
  val = straight(hand)
  if val > 0: return (5, val)
  val = threeOfAKind(hand)
  if val > 0: return (4, val)
  val = twoPair(hand)
  if val > 0: return (3, val)
  val = onePair(hand)
  if val > 0: return (2, val)
  return (1, max(map(cardvalue, hand)))
  
 
def winner(hand1, hand2):
  (ty1, val1) = rank(hand1)
  (ty2, val2) = rank(hand2)
  if ty1 > ty2:
    return 1
  elif ty2 > ty1:
    return 2
  elif ty1 == ty2 and val1 > val2:
    return 1
  elif ty1 == ty2 and val2 > val1:
    return 2
  else:
    return highcard(hand1, hand2)


assert(winner(['5H', 'QD', '2S', 'AC', '8C'], ['9H', 'KS', '7C', '4S', '3C']) == 1)

def winners():
  with open('poker.txt') as f:
    for line in f:
      cards = line.split()
      hand1 = cards[:5]
      hand2 = cards[5:]
      yield winner(hand1, hand2)

print('player1 wins %d hands' % sum(1 for x in winners() if x == 1))

#! /usr/bin/env python3

description = '''
Su Doku
Problem 96
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
'''

def zeros(board):
  return ((i,j) for i in range(0,9) for j in range(0,9) if board[i][j] == 0)

def rowvalues(board, i):
  return set(board[i][j] for j in range(0, 9) if board[i][j] != 0)

def colvalues(board, j):
  return set(board[i][j] for i in range(0, 9) if board[i][j] != 0)

def boxvalues(board, i, j):
  r0 = 3*(i//3)
  c0 = 3*(j//3)
  return set(board[r][c] for r in range(r0, r0 + 3) for c in range(c0, c0 + 3) if board[r][c] != 0)

def available(board, i, j):
  return set(range(1, 10)).difference(rowvalues(board, i), colvalues(board, j), boxvalues(board,i,j))

def mostConstrained(board):
  options = [(i,j, available(board, i,j)) for (i,j) in zeros(board)]
  return min(options, key=lambda x: len(x[2]))

def update(board, i, j, n):
  #return a copy of board, with position i,j updated to n
  return [row if r != i else [(x if c != j else n) for (c, x) in enumerate(row)] 
              for (r, row) in enumerate(board)]

def solve(board):
  # base case: solved once all zeros gone
  if all(board[i][j] != 0 for i in range(0, 9) for j in range(0, 9)):
    return board

  # recusrive case: try each available value in the most constrained position
  i,j,available = mostConstrained(board)
  for sln in (solve(update(board, i, j, n)) for n in available):
    if sln is not None: return sln

def readPuzzles():
  # each puzzle is 10 lines, starting with an initial header row
  with open('sudoku.txt','r') as f:
    lines = [line.strip() for line in f]
  return [[[int(d) for d in line] for line in lines[10*i+1 : 10*i+10]] for i in range(0, len(lines)//10)]
  
puzzles = readPuzzles()
solutions = [solve(puzzle) for puzzle in puzzles]
sumTopLeft3 = sum((sln[0][0]*100 + sln[0][1]*10 + sln[0][2]) for sln in solutions)
print(sumTopLeft3)


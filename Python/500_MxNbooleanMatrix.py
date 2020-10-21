import sys
from array import *

def min(a,b):
  return a if a < b else b

def move(puzzle,a,b,desta,destb,steps):
  # print(a,b)
  if (a < 0 or b < 0):
    return sys.maxsize
  if (a >= len(puzzle) or b >= len(puzzle[a])):
    return sys.maxsize
  if(puzzle[a][b] == 't'):
    return sys.maxsize
  if(a == desta and b == destb):
    return steps
  puzzle[a][b] = 't'
  steps += 1
  return min(min(move(puzzle,a - 1, b, desta, destb,steps),move(puzzle,a + 1, b, desta, destb,steps)),min(move(puzzle,a, b - 1, desta, destb,steps),move(puzzle,a , b + 1, desta, destb,steps)))

puzzle = [['f', 'f', 'f', 'f'],
          ['t', 't', 'f', 't'],
          ['f', 'f', 'f', 'f'],
          ['f', 'f', 'f', 'f']]

print(move(puzzle,3,0,0,0,0))




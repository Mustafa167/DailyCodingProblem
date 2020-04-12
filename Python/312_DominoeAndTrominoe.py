'''
312
You are given a 2 x N board, and instructed to completely cover the board with the following shapes:

    Dominoes, or 2 x 1 rectangles.
    Trominoes, or L-shapes.

For example, if N = 4, here is one possible configuration, where A is a domino, and B and C are trominoes.
'''

'''
arr -> main 2xN array
shape -> 0 = Dominoe, 1 = Trominoe
curCol -> Current column number, starts from zero
totalCol -> Total number for column
'''
def countTetris(shape,curCol,totalCol):

  if(curCol >= totalCol):
    return 0

  if(curCol == totalCol - 1):
    return 1

  #Trominoe need atleast three column to fill
  if(shape == 1) and (curCol > (totalCol - 4)):
    return 0


  return (countTetris(0,curCol + 1,totalCol) + countTetris(1,curCol + 3,totalCol))


def driverTetris(totalCol):
  return (countTetris(0,0 + 1,totalCol) + countTetris(1,0,totalCol))


N = 2
print(driverTetris(N))

'''
315
In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.

Here is an example:

1 2 3 4 8
5 1 2 3 4
4 5 1 2 3
7 4 5 1 2

Write a program to determine whether a given input is a Toeplitz matrix.
'''

def parseDiagnol(arr,rowIndex,colIndex,maxIndex):
  if rowIndex >= maxIndex and colIndex >= maxIndex:
    return True
  while rowIndex < maxIndex and colIndex < maxIndex:
    if arr[rowIndex][colIndex] != arr[rowIndex + 1][colIndex + 1]:
      return False
    rowIndex += 1
    colIndex += 1
  return True

def checkToeplitz(arr):
  rowLen = len(arr)
  for i in range(0,rowLen):
    for j in range(0,rowLen):
      if not parseDiagnol(arr,i,j,rowLen - 1):
        return False
  return True



A = [[1, 2, 3], 
     [4, 1, 2], 
     [3, 4, 1],]
print(checkToeplitz(A))


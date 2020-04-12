'''
310
Write an algorithm that finds the total number of set bits in all integers between 1 and N.
'''

import sys

def setBits(N):
  size = sys.getsizeof(N)
  count = 0
  for i in range(0,size):
    if(N & (1 << i)):
      count += 1  

  return count

print(setBits(24))

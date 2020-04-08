'''
309
There are M people sitting in a row of N seats, where M < N. Your task is to redistribute people such that there are no gaps between any of them, while keeping overall movement to a minimum.

For example, suppose you are faced with an input of [0, 1, 1, 0, 1, 0, 0, 0, 1], where 0 represents an empty seat and 1 represents a person. In this case, one solution would be to place the person on the right in the fourth seat. We can consider the cost of a solution to be the sum of the absolute distance each person must move, so that the cost here would be five.

Given an input such as the one above, return the lowest possible cost of moving people to remove all gaps.
'''
def getEmptySeats(occupiedSeats):
  length = len(occupiedSeats)
  j = 0
  for i in range(occupiedSeats[0],occupiedSeats[length - 1]):
    if i == occupiedSeats[j]:
      j += 1
    else:
      yield i

def rearrange(seats,source,target):
  seats[source] = 0
  seats[target] = 1
  #print("source: " + str(source))
  #print("target: " + str(target))

  #print("Rearrange: ",end='')
  #print(seats)
  return seats
   
def getOccupiedSeats(seats):
  count = 0;
  for item in seats:
    if item == 1:
      yield count
    count += 1

def minCost(seats,currIndex,maxLength,maxVal):
  #if all the elements exhausted
  #print(currIndex)
  if currIndex == maxLength:
    return maxVal

  occupiedSeats = list(getOccupiedSeats(seats))
  emptySeats = list(getEmptySeats(occupiedSeats))

  #print("Empty: " + str(len(emptySeats)))
  if not emptySeats:
    return 0

  minCostVal = minCost(seats,currIndex + 1,maxLength,maxVal)

  for val in emptySeats:
    costVal = minCost(rearrange(seats,occupiedSeats[currIndex],val),currIndex,maxLength,maxVal) + abs(occupiedSeats[currIndex] - val)
    if minCostVal > costVal:
      minCostVal = costVal
  
  return minCostVal


seats = [0, 1, 0, 0, 0 , 0, 1]
occupiedSeats = list(getOccupiedSeats(seats))
print(minCost(seats,0,len(occupiedSeats) - 1,len(seats)))





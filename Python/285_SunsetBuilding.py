def getNumberOfBuilding(arr):
  count = 1
  length = len(arr)
  for i in range(1,length):
    if(arr[i - 1] > arr[i]):
      count += 1
  return count

arr = [3, 7, 8, 3, 6, 1]
print(getNumberOfBuilding(arr))

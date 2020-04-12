'''
192
You are given an array of nonnegative integers. Let's say you start at the beginning of the array and are trying to advance to the end. You can advance at most, the number of steps that you're currently on. Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
'''

def checkPath(arr,index,lastIndex):
  if index == lastIndex:
    return True
  
  if index > lastIndex:
    return False

  isPath = False
  for i in range(1,arr[index] + 1):
    isPath |= checkPath(arr,index + i,lastIndex)

  return isPath


arr = [1, 2, 1, 0, 0]
print(checkPath(arr,0,len(arr) - 1))



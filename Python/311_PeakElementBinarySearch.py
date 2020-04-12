'''
311
Given an unsorted array, in which all elements are distinct, find a "peak" element in O(log N) time.

An element is considered a peak if it is greater than both its left and right neighbors. It is guaranteed that the first and last elements are lower than all others.
'''



def modifiedBinarySearch(arr,startIndex,endIndex):
  median = int((endIndex + startIndex)/2)

  #check if found a match
  if(arr[median] > arr[median + 1]) and (arr[median] > arr[median - 1]):
    return median

  if(arr[median] < arr[median + 1]) and (arr[median] > arr[median - 1]):
    return modifiedBinarySearch(arr,median + 1,endIndex)


  if(arr[median] > arr[median + 1]) and (arr[median] < arr[median - 1]):
    return modifiedBinarySearch(arr,startIndex,median - 1)  



arr = [1,3,5,10,2]

median = modifiedBinarySearch(arr,0,len(arr) - 1)
print(arr[median])

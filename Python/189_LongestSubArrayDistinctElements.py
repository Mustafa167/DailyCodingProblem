'''
189
Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
'''

numArray = [5, 1, 3, 5, 2, 3, 4, 1, 0]
hashArray = [0] * len(numArray)
maxCount = 1
count = 1

for num in numArray:
  if hashArray[num] != 1:
    hashArray[num] = 1
    count += 1
    if count > maxCount:
      maxCount = count
  else:
    hashArray = [0] * len(numArray)
    count = 1

print(maxCount)



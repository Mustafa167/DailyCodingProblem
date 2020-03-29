'''
197
Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.
'''
numData = [1, 2, 3, 4, 5, 6, 7, 8]
k = 5
lenData = len(numData)

rotatedData = [0] * lenData

for i in range(0,lenData):
  rotatedData[(i + k) % lenData] = numData[i]


print(rotatedData)

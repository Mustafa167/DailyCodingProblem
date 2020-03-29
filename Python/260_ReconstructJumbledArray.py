'''260. The sequence [0, 1, ..., N] has been jumbled, 
and the only clue you have for its order is an array representing whether each number is larger or smaller than the last. 
Given this information, reconstruct an array that is consistent with it. 
For example, given [None, +, +, -, +], you could return [1, 2, 3, 0, 4].'''
def returnNegative(signArray):
  negativeCount = 0
  for sign in signArray:
    if sign == '-':
      negativeCount += 1
  return negativeCount

def reconstructArray(signArray,negativeCount):
  numberArray = [];
  lastIncrease = negativeCount
  lastDecrease = negativeCount 
  for sign in signArray:
    if sign == 'None':
      numberArray.append(negativeCount)
    elif sign == '+':
      lastIncrease += 1
      numberArray.append(lastIncrease)
    elif sign == '-':
      lastDecrease -= 1
      numberArray.append(lastDecrease)
    
  return numberArray

signArray = ['None', '+', '+', '-', '-', '+']
negativeCount = returnNegative(signArray)
numberArray = reconstructArray(signArray,negativeCount);

for number in numberArray:
  print(number)

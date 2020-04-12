'''
202
Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.
'''

def isNumPallindrome(num):
  strNum = str(num)
  lenStrNum = len(strNum)

  for i in range(0,int(lenStrNum/2)):
    if strNum[i] != strNum[lenStrNum - i - 1]:
      return False

  return True


print(isNumPallindrome(111))



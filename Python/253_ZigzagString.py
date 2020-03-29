'''
253
Given a string and a number of lines k, print the string in zigzag form. In zigzag, characters are printed out diagonally from top left to bottom right until reaching the kth line, then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

t     a     g
 h   s z   a
  i i   i z
   s     g

'''

strData = "thisisazigzag"

K = 3
index = 0
increase = True
strList = ["" for x in range(K)]


for char in strData:
    for i in range(0,K):
      if index == i:
        strList[i] += char
      else:
        strList[i] += ' '
    
    if increase == True:
      index += 1
      if index == (K - 1):
        increase = False
    else:
      index -= 1
      if index == 0:
        increase = True


for i in range(0,K):
  print(strList[i])

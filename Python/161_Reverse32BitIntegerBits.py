'''
161
Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, return 0000 1111 0000 1111 0000 1111 0000 1111.
'''

def reverse(num):
  revNum = 0x00000000
  for i in range(0,32):
    if num & (1 << (31 - i)):
        revNum |= (1 << i)

  return revNum
      

num = 0x80000000
print(reverse(num))

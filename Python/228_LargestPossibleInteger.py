'''
228
Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. For example, given [10, 7, 76, 415], you should return 77641510.
'''
#Function gets the digit of number in string format
#num: Number in string format
#n: Nth place of digit
def get_nth_digit(num,n):
  if n >= len(num):
    return -1
  return(int(num[n])) 

# return negative if num1 is smaller than num2
def compare_digits(num1,num2):
  strData1 = str(num1)
  strData2 = str(num2)
  len1 = len(strData1)
  len2 = len(strData2)

  minlen = len1 if len1 < len2 else len2

  for i in range(0,minlen):
    if get_nth_digit(strData1,i) < get_nth_digit(strData2,i):
      return -1

  return 1

def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if compare_digits(arr[i - 1],arr[i]) == -1:
                swap(i - 1, i)
                swapped = True
                    
    return arr

numData = [10, 7, 76, 415]
sortedData = bubble_sort(numData)
print(''.join(str(x) for x in sortedData))



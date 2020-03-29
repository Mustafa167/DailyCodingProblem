
'''
256
Given a linked list, rearrange the node values such that they appear in alternating low -> high -> low -> high ... form. For example, given 1 -> 2 -> 3 -> 4 -> 5, you should return 1 -> 3 -> 2 -> 5 -> 4.
'''
import copy

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
      printval = self.headval
      while printval is not None:
        print (printval.dataval,end=' ')
        printval = printval.nextval


numlist = SLinkedList()
numlist.headval = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)

# Link first Node to second node
numlist.headval.nextval = e2
# Link second Node to third node
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5

print("Original list")
numlist.listprint()








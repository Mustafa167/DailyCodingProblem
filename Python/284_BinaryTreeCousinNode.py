# Helper function that allocates a   
# new node with the given data and  
# None left and right pairs.                                      
class newNode:  
    # Constructor to create a new node  
    def __init__(self, data):  
        self.data = data 
        self.left = None
        self.right = None


#function to get the level of the newNode
def getNodeLevel(node,data,level = 1):
  if(node == None):
    return 0

  if(node.data == data):
    return level

  retVal = getNodeLevel(node.left,data,level + 1)  

  if(retVal <= 0):
    return (getNodeLevel(node.right,data,level + 1)) 
  
  return retVal

#the function gets cousin nodes of "data"
#at given depth 
def getCousinNode(node,data,depth):

  if(node == None):
    return

  if(depth < 0):
    return
  
  if(depth == 0):
    yield node.data
  else:
    yield list(getCousinNode(node.left,data,depth - 1))
    yield list(getCousinNode(node.right,data,depth - 1))


root = newNode(3)  
root.left = newNode(2)  
root.right = newNode(5)  
root.left.left = newNode(1)  
root.left.right = newNode(4) 
root.right.right = newNode(6) 
root.right.left = newNode(7) 

data = 6
level = getNodeLevel(root,data)
cousins = list(getCousinNode(root,data,level - 1))
for cousin in cousins:
  print(cousin)

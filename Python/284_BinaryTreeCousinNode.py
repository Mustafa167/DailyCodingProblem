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
def getNodeLevel(node,data,level):
  if(node == None):
    return 0

  if(node.data == data):
    return level

  retVal = getNodeLevel(node.left,data,level + 1)  

  if(retVal <= 0):
    return (getNodeLevel(node.right,data,level + 1)) 
  
  return retVal



root = newNode(3)  
root.left = newNode(2)  
root.right = newNode(5)  
root.left.left = newNode(1)  
root.left.right = newNode(4) 
print(getNodeLevel(root,6,1))

'''
185
Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}

and

return 6.
'''

def get_intersection(point1,point2):
  if(point1[1] < point2[0]) or (point2[1] < point1[0]):
    return 0
  #partial overlap
  elif point1[1] > point2[0] and point1[1] < point2[1]:
    print("here1")    
    return point1[1] - point2[0]
  elif point2[1] > point1[0] and point2[1] < point1[1]:
    print("here2")    
    return point2[1] - point1[0]
  #full overlap
  elif point1[0] > point2[0] and point1[0] > point2[1]:
    print("here3")
    point2[1] - point2[0]
  elif point2[1] > point1[0] and point2[1] > point1[1]:
    print("here4")
    point1[1] - point1[0]
  
  


print(get_intersection((4,7),(5,8)))


square1 = {
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}

square2 = {
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}

pointx1 = [square1["top_left"][0],square1["top_left"][0] + square1["dimensions"][0]]
pointx2 = [square2["top_left"][0],square2["top_left"][0] + square2["dimensions"][0]]
pointy1 = [square1["top_left"][1],square1["top_left"][1] + square1["dimensions"][1]]
pointy2 = [square2["top_left"][1],square2["top_left"][1] + square2["dimensions"][1]]

print(pointx1)
print(pointx2)
print(pointy1)
print(pointy2)

#print(get_intersection(pointx1,pointx2))
#print(get_intersection(pointy1,pointy2))




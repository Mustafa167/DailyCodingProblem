friends = {0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]} 

#intialize groups
group = [-1] * len(friends)
index = -1
for count in friends:
  #check if the group is new or already exits
  if(group[count] == -1): 
    index += 1
    group[count] = index
  else:
    index = group[count]

  #group all the related frends
  for friend in friends[count]:
    group[friend] = index

friends.clear()
length = len(group)
for i in range(0,length):
  if(friends.get(group[i]) == None):
    friends[group[i]] = [i]
  else:
    friends[group[i]].append(i)

print(friends)




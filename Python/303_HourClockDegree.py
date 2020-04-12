'''
303
Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?
'''


stepHour = int(360/12) 
stepMinute = int(360/60)

timeStamp = "15:03".split(':')
degreeHour = (int(timeStamp[0]) % 12) * stepHour
degreeMinute = int(timeStamp[1]) * stepMinute
diff = abs(degreeHour - degreeMinute)
if diff > 180:
  diff -= 360

print(abs(diff))

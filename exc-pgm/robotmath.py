"""A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT. program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer"""

#import math 

import math
#initiate the robot position
pos = [0,0]
while True:
    s = input()
    if not s:
        break
#movement can be split using whitespace

    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass
#calculate the traveling position and print the answer 

print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))

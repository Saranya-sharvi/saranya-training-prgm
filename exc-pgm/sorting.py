"""make the program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score"""
#importing itemgetter is used to enable multiple sort
from operator import itemgetter, attrgetter

l = []
while True:
    s = input()
    if not s:
        break
#append the user input and it is splited under comma
    l.append(tuple(s.split(",")))
#print the appropriate result
print(sorted(l, key=itemgetter(0,1,2)))

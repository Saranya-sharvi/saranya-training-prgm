"""write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24] and also to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155]"""

#assign the list value

li = [5,6,77,45,22,12,24]

#remove the even numbers

li = [x for x in li if x%2!=0]

#print the list after removing even numbers

print(li)

#assign the list value

li = [5,6,77,45,22,12,24,35,70,88,120,155]

#remove the divisible by 5 and 7

li = [x for x in li if x%5!=0 and x%7!=0]

#print the list after removing the values

print(li)

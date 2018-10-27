"""write a program generate a 3*5*8 3D array whose each element is 0"""


#Using list comprehension to make an array

array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]

#print the 3d array

print(array)

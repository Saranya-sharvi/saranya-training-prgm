"""make the program which takes 2 digits, x,y as input and generates a 2-dimensional array"""
input_str = input()
dimensions=[int(x) for x in input_str.split(',')]
#the element value in the i-th row and j-th column of the array should be i*j. 
rowNum=dimensions[0]
colNum=dimensions[1]
#if i=0,1....,x-1;j=0,1...y-1
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

#assign the row and column range
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col
#print the result
print(multilist)

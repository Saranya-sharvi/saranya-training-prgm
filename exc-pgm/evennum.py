"""make the program to find all such numbers between 1000 and 3000 such that each digit of the number is an even number"""

oddvalues = []
evenvalues = []
for i in range(3001, 3090):
    #make to find the result using and operator
    if (i%2==0):
        evenvalues.append(i)
    else:
        oddvalues.append(i)
#print the appropriate result
print(evenvalues)

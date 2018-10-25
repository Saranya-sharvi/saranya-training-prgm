"""Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included) and print first 5 values as well only print last 5 values"""


def printTuple():
	li=list()
	for i in range(1,20):
		li.append(i**2)

#print the square values between 1 and 20

	print(tuple(li))	
		
#print the first 5 values 
	
	print(tuple(li[:5]))

#print the last 5 values

	print(tuple(li[-5:]))
		
printTuple()








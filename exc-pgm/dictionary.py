"""Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys and  just print the values only and also again just print the keys only, and print first 5 values as well last 5 values in seperatedly using list"""

def printDict():

#assign the dictionary
	
	d=dict()

#perform the square value of keys 

	
	for i in range(1,21):

		d[i] = i**2

#print the values only

	print(d)
	s = []
	for (k,v) in d.items():	
		s.append(v)	
	print("generate only the values:", s)
	
#print the keys only	
	
	a = []
	for k in d.keys():	
		a.append(k)
	print("generate only the keys:", a)
	
#print first 5 values only
	
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li[:5])
	
#print last 5 values only
	
	print(li[-5:])
printList()	
	print(li[5:])
printList()	
	
	
#print the both keys and values in dictionary

printDict()

"""def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li[5:])
		

printList()"""





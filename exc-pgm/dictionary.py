"""Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys and then just print only the values as well keys in seperatedly"""

def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	print(d)
	
#The function should just print the values only.	
	
	for (k,v) in d.items():	
		print("\n generate only value", v)	
		
#The function should just print the keys only.		
	
	for k in d.keys():	
		print("\n", "generate only keys", k)			
		

printDict()











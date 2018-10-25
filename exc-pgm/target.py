


#Create an empty list

"""task = [] 
print("Enter 10 Numbers seperate using enter: ")
for i in range(10):
	task.append(eval(input()))
	#number = i
	#print("no.of single digits: ",len(str(number)))
	
	
print(task)"""


"""n=task
count=0
while(n!=0):
    count=count+1
    n=n%10
print("The number of digits in the number are:",count)

num=list(task(i))
mod=num%2
	
if(num%2) > 0:
	print("odd number")
else:
	print("even number")"""


class Calc():
	def oddeve(task):
		num = task
		if(num%2 == 0):
			print("{0}is even".format(num))
		else:
			print("{0}is odd".format(num))

		
task = [] 
print("Enter 10 Numbers seperate using enter: ")
for i in range(10):
	task.append(eval(input()))
print(task)

for ts in task:
	print(Calc.oddeve(ts))

		






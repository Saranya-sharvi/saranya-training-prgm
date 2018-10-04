number=int(input("Enter the number:"))
factorial=1
if number>0:
		for i in range(1,number+1):
			factorial=factorial*i
		print("factorial of",number,"is",factorial)
elif number==0:
		print("factorial of 0 is 1")

else:
		number<0
		print("dsnt find fact for neg numbers")	

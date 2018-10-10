print("Find biggest values amoung three values: ")
var1 = int(input("enter var1: "))
var2 = int(input("enter var2: "))
var3 = int(input("enter var3: "))

if((var1 >= var2 )and (var1 >= var3)):
	
	print("The biggest is :", var1)

if(var2 >= var3):
	print("The biggest is :", var2)

else:
	print("The biggest is :", var3)

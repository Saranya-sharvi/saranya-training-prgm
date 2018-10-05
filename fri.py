string=raw_input("Enter input:")
count1=0
count2=0
count3=0
for i in string:
	if(i.isdigit()):
		count1=count1+1
	if(i.isalpha()):
		count2=count2+1
	count3=count1+count2
print("the number of digits is:")
print(count1)
print("the number of char is:")
print(count2)
print("the number of str is:")
print(count3) 
 
	
	

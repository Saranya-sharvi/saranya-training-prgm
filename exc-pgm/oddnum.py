""" make the program to get number of integer values from user seperated usinf comma and then print only the odd numbers"""
values = input()
#split the odd numbers among user input
numbers = [x for x in values.split(",") if int(x)%2!=0]
#print the appropriate result
print(",".join(numbers))

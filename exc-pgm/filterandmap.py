
"""Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included) and which can map() to make a list whose elements are square of numbers between 1 and 20 (both included)"""



#print even number square value


evenNumbers = filter(lambda x: x%2==0, range(1,21))
print(evenNumbers)


#print the whole list square value

squaredNumbers = map(lambda x: x**2, range(1,21))
print(squaredNumbers)



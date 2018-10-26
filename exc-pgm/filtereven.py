"""make program that can filter even numbers in a list by using filter function and which can map() the square of elements in the list and also map() and filter() the even numbers in the list using lambda to define anonymous functions"""

#create list value

li = [1,2,3,4,5,6,7,8,9,10]

#filter the even numbers

evenNumbers = filter(lambda x: x%2==0, li)

#map the square numbers

squaredNumbers = map(lambda x: x**2, li)

#filter the square even numbers

squareevenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))

#print the results

print("even numbers are: ", evenNumbers)
print("square numbers are: ", squaredNumbers)
print("square evennumbers are: ", squareevenNumbers)



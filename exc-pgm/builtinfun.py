"""write a program to print some Python built-in functions documents,such as abs(), int(),raw_input() and add document for your own function"""

print abs.__doc__
print int.__doc__
print raw_input.__doc__


def square(num):

#Return the square value of the input number.
    
#The input number must be integer.
    
    return num ** 2

print square(7)
print square.__doc__

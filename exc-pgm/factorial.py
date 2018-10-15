"""compute the factorial of the user input number"""
def fact(x):
    if x == 0:
        return 1
#factorial calculation part of given number
    return x * fact(x - 1)
#assign the value to given input
x=input(int())
#print the factorial value of given number
print(fact(x))					

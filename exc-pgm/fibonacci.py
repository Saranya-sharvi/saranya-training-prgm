"""write a program to compute the value of f(n) with a given n input by console using fibonacci sequence and also using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console"""


#define the function

def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

#getting console input

n=int(input("enter the value to find fibonacci series : ", ))

#fibonacci series formate

values = [str(f(x)) for x in range(0, n+1)]
print(",".join(values))


#print result

print("result is: ", f(n))


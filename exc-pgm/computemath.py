"""Write a program to compute:
f(n)=f(n-1)+100 when n>0
and f(0)=1
with a given n input by console (n>0)"""

#define a function

def f(n):
    if n==0:
        return 0
#calculating the value of n
    else:
        return f(n-1)+100
#getting a console input

n=int(input())

#print the result of f(n) value

print(f(n))


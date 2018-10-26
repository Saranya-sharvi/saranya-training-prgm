"""Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0)"""

#getting console input

n=int(input())
#declare sum value

sum=0.0
#range of value

for i in range(1,n+1):

#conversion of int into float using float()

    sum += float(float(i)/(i+1))

#print result

print(sum)


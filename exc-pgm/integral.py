"""make a program to generate a dictionary that contains (i,i*i) such that is an integral number between 1 and n"""
n=input(int())
d=dict()
#assign the range of i
for i in range(1,n+1):
    d[i]=i*i
#print the result in the form of dictionary
print(d)

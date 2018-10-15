"""make a program to find all such numbers which are divisible by7 but are not a multiple of 5 between 2000 to 3000"""
l=[]
for i in range(2000, 3000):
#codition can applied using 'and' operator
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
#print the result
print(','.join(l))

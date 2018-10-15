"""perform mathematical calculation"""
import math
#assign the default values of c and h
c=50
h=30
value = []
#splitting can done after getting the input value
items=[x for x in input().split(',')]
for d in items:
#performing the calculation
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
#print the result after mathematical operation performing
print(','.join(value))

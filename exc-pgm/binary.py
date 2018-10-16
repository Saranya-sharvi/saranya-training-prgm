"""make a program that accepts a sequence of comma separated 4digit binary numbers as its input and then check whether they are divisible by 5 or not and then only the divisible numbers printed in comma separated sequence"""
value = []
#split the user input using comma
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
#check the binary numbers that are divisible by 5 using not keyword
    if not intp%5:
        value.append(p)
#print the result
print(','.join(value))

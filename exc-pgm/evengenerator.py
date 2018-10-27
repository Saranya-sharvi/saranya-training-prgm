"""write a program using generator to print the even numbers between 0 and n in comma separated form and also to print the numbers which can be divisible by 5 and 7 between 0 while n is input by console"""

#using Evengenerator as a function

def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1
n=int(input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print(",".join(values))
        
        
#using Numgenerator as a function        
        
def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            
# yield used to produce the next value in generator.
            
            yield i
            
n=int(input())
values = []
for i in NumGenerator(n):
    values.append(str(i))

print(",".join(values))







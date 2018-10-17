""" make the program that define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n"""

class string_handling():
#using function to perform divise operation

    def putNumbers(n):
        divise = []
        for i in range(1, n+1):
            if i%7==0:
                divise.append(i)

        return divise
#using another function to perform reverse operation

    def st_rev(n):
        s = str(n)[::-1]
        return s
#get one integer from user to perform above mentioned operations

n = int(input())
#function calling can perform 

b = string_handling.putNumbers(n)
c = string_handling.st_rev(n)
#print the appropriate result

print("Reverse",c)
print("numbers divisible by 7",b)

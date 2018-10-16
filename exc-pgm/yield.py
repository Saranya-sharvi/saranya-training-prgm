
class string_handling():
    def putNumbers(n):
        divise = []
        for i in range(1, n+1):
            if i%7==0:
                divise.append(i)

        return divise

    def st_rev(n):
        s = str(n)[::-1]
        return s

n = int(input())
b = string_handling.putNumbers(n)
c = string_handling.st_rev(n)
print("Reverse",c)
print("numbers divisible by 7",b)

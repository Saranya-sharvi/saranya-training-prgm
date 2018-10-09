class maths():
    def division(a,b):
        c=a%b
        return c
    def addition(a,b):
        c=a+b
        return c
    def subtaction(a,b):
        c=a-b
        return c

a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))

ans={}
ans["division"]=maths.division(a,b)
ans["addition"]=maths.addition(a,b)
ans["subtraction"]=maths.subtaction(a,b)

print("result is:",ans)  
    

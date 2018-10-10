



""" assign of class"""
class math():
    """ perform division operation """

    def division(a,b):
        c=a/b
        return c
    """ perform addition operation """

    def addition(a,b):
        c=a+b
        return c
    """ perform subtraction operation """

    def subtaction(a,b):
        c=a-b
        return c
    """get the input from user"""


a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))

    
ans={}
#ans["division"]=math.division(a,b)
ans["addition"]=math.addition(a,b)
ans["subtraction"]=math.subtaction(a,b)

print("result is:",ans)  
    

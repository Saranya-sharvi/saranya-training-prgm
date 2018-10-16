"""make the program that computes the value of a+aa+aaa+aaaa"""
#get a integer from user
a = input()
#find the a+aa+aaa+aaaa value for given input 
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
#print the appropriate result
print(n1+n2+n3+n4)

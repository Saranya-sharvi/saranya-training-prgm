"""make the program which accepts a string as input to print "Yes" if the string is "yes" or "YES" otherwise print No"""

#to get console input
 
s= input()

#using or operator to check the input like yes or YES or anything and print the result

if s=="yes" or s=="YES" or s=="Yes":
    print("Yes")

else:
    print("No")



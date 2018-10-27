"""write a program which accepts a string from console and print the characters that have even indexes"""

#get console input

s=input()

#Use list[::2] to iterate a list by step 2
s = s[::2]

#print the appropriate result

print(s)

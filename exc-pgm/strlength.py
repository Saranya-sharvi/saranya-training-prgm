"""Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line"""

def printValue(s1,s2):

#assign the values of s1 and s2

	len1 = len(s1)
	len2 = len(s2)
#conditions can be applied to print the result

	if len1>len2:
		print(s1)
	elif len2>len1:
		print(s2)
	else:
		print(s1)
		print(s2)
		
#put the values to s1 and s2

printValue("saran","tree")

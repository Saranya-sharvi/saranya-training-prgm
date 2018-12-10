"""import sys
filename = input("Input the File: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))"""


"""import sys
print "This is the name of the script: ", sys.argv[0]
print "Number of arguments: ", len(sys.argv)
print "The arguments are: " , str(sys.argv)"""



import sys
import os
#st = os.stat("hai.csv")


#print("find file extension: ")

#print("This is the extension of the file :",(sys.argv[1]))
word = str(sys.argv[1])
text = word.split('.')

#print(text[1])
if text[1] == "html":
	print("this is html file")
elif text[1] == "py":
	print("this is python file")
else:
	print("this is text file")	
#print(result.split('. ')




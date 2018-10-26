"""Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only"""


#import regex

import re

#getting user input seperate using whitespace

s = input()

#using re.findall() to find all substring using regex

print(re.findall("\d+",s))


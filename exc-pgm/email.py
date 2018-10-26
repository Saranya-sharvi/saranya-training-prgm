"""Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address and also print the companyname of a given email address Both user names and company names are composed of letters only"""

import re

#getting email into console input

emailAddress = raw_input()

#use \w to match letters

pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2,emailAddress)


pat3 = "(\w+)@(\w+)\.(com)"
r3 = re.match(pat3,emailAddress)

#print the result

print r3.group(2)
print r2.group(1)

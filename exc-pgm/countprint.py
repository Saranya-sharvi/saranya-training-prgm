"""write a program which count and print the numbers of each character in a string input by console"""


#Use dict to store key/value pairs

dic = {}
s=input()
for s in s:

#Use dict.get() method to lookup a key with default value

    dic[s] = dic.get(s,0)+1

#print the appropriate result

print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))

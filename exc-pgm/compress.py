 """write a program to compress and decompress the string "hello world!hello world!hello world!hello world!" """

#import zlib

import zlib

#value assign the string

s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)

#print compress and decompress 

print t
print zlib.decompress(t)


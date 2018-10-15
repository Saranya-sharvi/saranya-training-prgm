"""take a input from user,input like a paragraph"""
s = input()
#split the words using whitespace
words = [word for word in s.split(" ")]
#print the result after removing all duplicate words and sorting the remaining words in alphanumerically
print(" ".join(sorted(list(set(words)))))

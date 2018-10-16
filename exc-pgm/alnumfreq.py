freq = {}   # frequency of words in text
line = input()
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
words.sort(w)

for w in words:
    print("%s:%d" % (w,freq[w]))

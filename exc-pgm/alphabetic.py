""" to get input as sequence of words"""
items=[x for x in input().split(',')]
#sorting the input in the form of alphabetical
items.sort()
#print the words after sorting
print(','.join(items))

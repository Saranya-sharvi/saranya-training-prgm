"""write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list"""

#import math function

import math
def bin_search(li, element):

#assign the default value of top,bottom and index

    bottom = 0
    top = len(li)-1
    index = -1
    
#find the index of the given list
    
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index
#assign the list and list value

li=[2,5,7,9,11,17,222]

#print the position of the given value

print(bin_search(li,17))
print(bin_search(li,12))







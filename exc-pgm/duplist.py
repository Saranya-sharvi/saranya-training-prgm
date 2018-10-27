"""With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved"""



def removeDuplicate( li ):
    newli=[]

#Use set() to store a number of values without duplicate.

    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)

    return newli

#list assigning with values

li=[12,24,35,24,88,120,155,88,120,155]

#print the result after removing the duplicates

print(removeDuplicate(li))

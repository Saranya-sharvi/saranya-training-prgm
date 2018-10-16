"""make the program that accepts a sentence and calculate the number of letters and digits as well to calculate the number of upper case letters and lower case letters"""

s = input()
d={"DIGITS":0, "LETTERS":0, "UPPER CASE":0, "LOWER CASE":0}
for c in s:
#check whether a input is digit/alpha
    if c.isdigit():
        d["DIGITS"]+=1 
    elif c.isalpha():
#check whether a alpha is lowercase/uppercase
        if c.islower():
            d["LOWER CASE"]+=1
        
        elif c.isupper():
            d["UPPER CASE"]+=1

        d["LETTERS"]+=1 
    else:
        pass
#print the results

print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])
print("UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])

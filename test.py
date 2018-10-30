"""print("Find biggest values amoung three values: ")
var1 = int(input("enter var1: "))
var2 = int(input("enter var2: "))
var3 = int(input("enter var3: "))

if((var1 >= var2 )and (var1 >= var3)):
	
	print("The biggest is :", var1)

if(var2 >= var3):
	print("The biggest is :", var2)

else:
	print("The biggest is :", var3)"""











def count_substring(string, sub_string):
    cnt = 0
    len_ss = len(sub_string)
    for i in range(len(string) - len_ss + 1):
        if string[i:i+len_ss] == sub_string:
            cnt += 1
    return cnt






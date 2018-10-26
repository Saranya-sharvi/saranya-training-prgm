"""to write a python code to get user input and then performs following operations using class functions and the results should store in dictionary after the dictionary convert into json file formate
(i)find total items (ii)find center item (iii)find total sum (iv)find even numbers (v)find odd numbers (vi)find biggest number (vii)find smallest number (viii)find asending order (ix)find desending order (x)find 1digit numbers (xi)find 2digit numbers (xii)find 3digit numbers (xiii)find 4digit numbers (xiv)find 5digit numbers (xv)find 5more digit numbers (xvi)find disible by 7 (xvii)find sum divisible 7"""


import json



class task():
    def inp_check(s):
        if s[-1]==',' and s[0]==',':
            print("yes both")
            list = s.split(',')[:-1][:0]
            new_list=[]
            for num in list:
                new_list.append(int(num))
            return new_list
        elif s[-1]==',':
            print("yes after")
            list = s.split(',')[:-1]
            new_list=[]
            for num in list:
                new_list.append(int(num))
            return new_list
        elif s[0]==',':
            print("yes before")
            list = s.split(',')[:0]
            new_list=[]
            for num in list:
                new_list.append(int(num))
            return new_list
        else:
            list = s.split(',')
            new_list=[]
            for num in list:
                new_list.append(int(num))
            return new_list
#find odd even 

    def odd_even(list):
        out = {}
        even_list = []
        odd_list  = []
        for num in list:
            if num%2==0:
                even_list.append(num)
            else:
                odd_list.append(num)
        out["even_num"] = even_list
        out["odd_num"]  = odd_list

        return out

#find sum of list


    def sum_of_list(list):
        sums = 0
        for num in list:
            sums = sums + num

        return sums

#find1,2,3,4,5and 5 more digits

    def find_digits(list):
        dict_digits = {}
        list_dig_1 =[]
        list_dig_2 =[]
        list_dig_3 =[]
        list_dig_4 =[]
        list_dig_5 =[]
        list_dig_more_5 =[]
        for num in list:
            if len(str(num)) == 1:
                list_dig_1.append(num)
            elif len(str(num)) == 2:
                list_dig_2.append(num)
            elif len(str(num)) == 3:
                list_dig_3.append(num)
            elif len(str(num)) == 4:
                list_dig_4.append(num)
            elif len(str(num)) == 5:
                list_dig_5.append(num)
            else:
                list_dig_more_5.append(num)

        dict_digits["one_digit"] = list_dig_1
        dict_digits["two_digit"] = list_dig_2
        dict_digits["three_digit"] = list_dig_3
        dict_digits["four_digit"] = list_dig_4
        dict_digits["five_digit"] = list_dig_5
        dict_digits["five_more_digit"] = list_dig_more_5

        return dict_digits

#find divisible 7 and sum of divisible 7
    
    def div_7(list):
    	store={}
    	sum_list=[]
    	for num in list:
    		if num%7 == 0:
    			sum_list.append(num)
    	
    	store["div_7"] = sum_list
    	store["sum_div_7"] = task.sum_of_list(sum_list)
    	return store

#find center value
    
    def center_value(list):
    	cen_list=[]
    	f_len = len(list)%2
    	if f_len == 0:
    		ss = int(len(list)/2)
    		center = ss - 1
    		center_two = ss
    		cen_list.append(list[center])
    		cen_list.append(list[center_two])

    	else:
    		save = int(len(list)/2)
    		cen_list.append(list[save])
    		
    	return cen_list
			

#input getting 

print("enter numbers with comma (,) separated")
s = input()
list = task.inp_check(s)
result = {}


#function calling

oddeven = task.odd_even(list)
result["total_items"] = len(list)
result["center_item"] = task.center_value(list)
result["total_sum"]   = task.sum_of_list(list)
result["even"]  = oddeven["even_num"]
result["odd"]   = oddeven["odd_num"]
result["biggest"]  = max(list)
result["smallest"] = min(list)
result["asending"] = sorted(list, key=int)
result["desending"] = sorted(list, key=int, reverse=True)
digit = task.find_digits(list)
result["1_digits"] = digit["one_digit"]
result["2_digits"] = digit["two_digit"]
result["3_digits"] = digit["three_digit"]
result["4_digits"] = digit["four_digit"]
result["5_digits"] = digit["five_digit"]
result["5_more_digits"] = digit["five_more_digit"]
sss = task.div_7(list)
result["divisible_7"] = sss["div_7"]
result["sum_divisible_7"] = sss["sum_div_7"]

#json formate conversion

with open('saran.json', 'w')as task:
	
	json.dump(result,task)
#result printing

print(result)


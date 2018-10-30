import json

class task():
	def lower(list):
		l=list.lower()
		return l
		
	def upper(list):
		m=list.upper()
		return m	
	
	def center(list):
		n=int((len(list)/2) - 1)
		#print(n)
		string = list[n]
		return string
		
	def position(list, x):
		if s1 in list:
			p = int(list.index(s1)) + 1
			return p
		
	def dig_alnum(list):
		result = {}
		dig_list = []
		alnum_list = []
		for x in list:
			#print(x)
			if (x.isalpha())==True:
				alnum_list.append(x)
			else:
				dig_list.append(x)
				
		result["alphanumeric"] = alnum_list
		result["digit"] = dig_list
		return result
		
		
	def split(list):
		s=list.split()
		return s
					
	
	
print("enter the string")
v = input()
list = task.lower(v)
	
answer = {}

answer["lower"] = task.lower(list)
answer["upper"] = task.upper(list)
answer["center"] = task.center(list)
print("enter the char to find the position")
s1 = input()
#print("s1 not in v plz provide a valid string")

answer["position"] = task.position(list, s1)
digalnum = task.dig_alnum(list)
answer["alphanumeric"] = digalnum["alphanumeric"]
answer["digits"] = digalnum["digit"]  
answer["split"] = task.split(list)


with open('stroper.json', 'w')as task:
	json.dump(answer, task) 

print(answer)
	
	
	

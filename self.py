class human():
	
	
	
	
	#def __init__(self,name="noname",age=0,nationality="nonationality",gender="nogender"):
	
	
	def __init__(self,name,age,nationality,gender):
	
		self.name=name
		self.age=age
		self.nationality=nationality
		self.gender=gender
	def answer(self):
		print("hello, my name is:", self.name)
		print("my age is:", self.age)
		print("my nationality is:", self.nationality)
		print("my gender is:", self.gender)
		
		
		
		
sugu=human("sugu",31,"india","male")
renu=human("renu",24,"india","female")


print("\n", "sugu's attributes:")
print(sugu.name)
print(sugu.age)
print(sugu.nationality)
print(sugu.gender)


print("\n", "sugu's methods:")
sugu.answer()



print("\n", "renu's attributes:")
print(renu.name)
print(renu.age)
print(sugu.nationality)
print(renu.gender)

print("\n", "renu's methods:", "\n")
renu.answer()



	

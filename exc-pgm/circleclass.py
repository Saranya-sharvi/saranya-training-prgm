"""Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area"""

#define a class

class Circle(object):

#define a function

	def __init__(self, r):
		self.radius = r
	def area(self):
		return self.radius**2*3.14

aCircle = Circle(2)

#print result
print(aCircle.area())


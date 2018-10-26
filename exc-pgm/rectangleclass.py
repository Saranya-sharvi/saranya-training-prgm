"""Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area"""


#define a class

class Rectangle(object):

#define a function
    def __init__(self, l, w):
        self.length = l
        self.width  = w

#calculate the area of rectangle

    def area(self):
        return self.length*self.width

#value assign to length and width

aRectangle = Rectangle(2,10)

#print the result

print(aRectangle.area())


"""Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default"""

#define a shape class

class Shape(object):
    def __init__(self):
        pass

#define area function

    def area(self):
        return 0

#define subclass like square

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

#define area function

    def area(self):
        return self.length*self.length
#assign the length value

aSquare= Square(5)

#print the result

print(aSquare.area())

#raise RuntimeError('something wrong')


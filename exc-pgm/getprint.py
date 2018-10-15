"""make the program using class which has atleast 2methods and also include simple test function to test the class methods"""
class InputOutString(object):
    def __init__(self):
        self.s = ""
#using getstring method to get a string from console input
    def getString(self):
        self.s = input()
#using printstring method to print the string in upper case
    def printString(self):
        print self.s.upper()
#object creation used to calling the above 2 functions
strObj = InputOutString()
strObj.getString()
strObj.printString()

"""Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class"""


#assigning the class with function

class Person(object):
    def getGender( self ):
        return "Unknown"

class Male( Person ):
    def getGender( self ):
        return "Male"

class Female( Person ):
    def getGender( self ):
        return "Female"

#function calling can perform

aMale = Male()
aFemale= Female()

#print the appropriate result

print(aMale.getGender())
print(aFemale.getGender())


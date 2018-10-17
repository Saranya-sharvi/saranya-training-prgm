 """make the program to define a class, which have a class parameter and have a same instance parameter"""

class Person:

# Define the class parameter "name"

    name = "Person"
    
    def init(self, name = None):

# self.name is the instance parameter

        self.name = name

saranya = Person()
saranya.name = "Saranya"
print "%s name is %s" % (Person.name, saranya.name)

renu = Person()
renu.name = "Renu"
print "%s name is %s" % (Person.name, renu.name)




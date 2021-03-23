class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Use the Person class to creat an object, and then exec the printname method:

x = Person("Jorgey", "Porgey")
x.printname()

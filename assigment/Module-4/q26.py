# Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

class stud:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(stud):
    pass

x = Student("Mike", "Olsen")
x.printname()
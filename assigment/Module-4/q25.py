# What relationship is appropriate for Student and Person?

class Person:   
    def __init__( self, name, surname ):   
        self.name = name   
        self.surname = surname   
    def greet( self ):   
        print( "My name is " + self.name + " " + self.surname )   

class Student( Person ):   
    def __init__( self, name, surname, studentNo ):   
        super().__init__( name, surname )   
        self.studentNo = studentNo   

person = Person( "John", "Doe" )   
person.greet()   

student = Student( "Bob", "Doe", 152 )   
student.greet()  
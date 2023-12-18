# What is Instantiation in terms of OOP terminology?


"Instantiation: When you instantiate a class, you create an object based on that class. The process involves allocating memory for the object, initializing its attributes (if any), and returning a reference to the newly created object."

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

# Instantiating two Car objects
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")

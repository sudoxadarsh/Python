"""
Class : A blueprint for creating objects that combines data(attributes) and
behaviour (methods)

Object: AN instances of a class. 
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

s1 = Student("Adarsh", 22)
s1.display()

print(f"data that object of class holds: {s1.display()}")


"""
class : Define a class.
__init__() : initializes an object's attributes.
s1 : An object of the Student class

"""

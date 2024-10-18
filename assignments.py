
"""OOP or Object Oriented Program is based on concept of objects that contain both methods and data. OOP
has 4 pillars: abstraction, encapsulation,inheretance and polymorphism.
OOP has so many advantages such as:
__It is easier and faster to execute, it has a clean and clear structure for developers and it helps 
to make  reuseble codes that can be maintain, modify and debug easily.
"""

class car:
    def Model(self):
        return "This is a Tesla Product"

class Motorbike:
    def Model(self):
        return "This is a product of BMW K1600"

def Vehicles_Model(Vehicles):
    print(Vehicles.Model())

Vehicles_Model(car())
Vehicles_Model(Motorbike())



#  Class:
"""A class is a blueprint for creating objects in OOP. It defines a set of attributes (data) and methods (functions)
   that the created objects will have. For example, a Car class might have attributes like color and model, and methods 
   like drive() and stop()."""

class car:
    def __init__(self, name, color):
        self.name = name  
        self.color = color 

    def stop(self):
        return f"{self.name} car with {self.color} color is stopped!"
    


# Object:
"""An object is an instance of a class. It represents a specific entity with its own state and behavior defined by the class.
   For example, if Car is a class, then my_car could be an object of that class with specific values for its attributes 
   (like color: red, model: Toyota)."""
 
 
my_car = car("Tesla", "red")

print(my_car.name)  
print(my_car.color)  
print(my_car.stop())  

# Constructor:
"""A constructor is a special method in a class that is automatically called when an object is created.
   It initializes the object's attributes. In Python, the constructor is defined using the __init__ method. """

class cloth:
    def __init__(self, model, color):
        self.model = model 
        self.color = color 
    def wearing(self):
        return f"The cloth with model of {self.model} and color of {self.color} is exist in our store."
    
shirt = cloth("T-shirt","light_blue")
skirt = cloth("long_skirt","gray")
coat = cloth ("Trench coat","brown")

print(skirt.color)
print(shirt.model)
print(coat.color)
print(coat.wearing())
print(skirt.wearing())
print(shirt.wearing())

#  Inheritance:
"""Inheritance is a mechanism in OOP that allows one class (child or subclass) to inherit attributes and methods from
  another class (parent or superclass). This promotes code reuse and establishes a hierarchical relationship between classes."""

class animal:
    def sound(self):
        print("It is talking")

class bird(animal): 
    def speak(self):
        print("it is chirping")


# Concatenation
    """Concatenation refers to the operation of joining two or more strings or sequences together. In Python,
      this can be done using the + operator for strings"""
    
    names = "Deeba"
    last_names ="Omarzad"
    result = names +" " + last_names
    print (result)


#  self keyword
    """The self keyword in Python refers to the instance of the class itself. It is used within class methods to access
      attributes and methods associated with the specific object created from the class."""

class animals:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} says Woof!")

dog= animals("Dog")
print(dog.name)
print(dog.sound())




#  File Handling
"""File handling refers to the process of reading from and writing to files in programming. In Python, this can be done using 
  built-in functions like open(), read(), write(), and close(). File handling allows you to store data persistently outside of
 your program's memory"""

# Example of writing to a file
with open('example.txt', 'w') as file:
     file.write("Hello, World!")

# Example of reading from a file
with open('example.txt', 'r') as file:
    content = file.read()


#  NumPy
"""NumPy (Numerical Python) is a powerful library in Python used for numerical computing. It provides support for arrays,
matrices, and many mathematical functions to operate on these data structures efficiently. NumPy is widely used in data analysis,
scientific computing, and machine learning due to its performance advantages over standard Python lists."""

import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr) 

'''Write a program to create an abstract class Vehicle. Derive three classes Car,
Motorcycle and Truck from it. Define appropriate methods and print the details
of vehicle.'''
from abc import ABC, abstractmethod
class Vehicle:
    def __init__(self,name,colour,price):
        self.name = name
        self.colour = colour
        self.price = price
    @abstractmethod
    def display(self):
        print(f"Name :- {self.name}")
        print(f"Price :- {self.price}")
        print(f"Colour :- {self.colour}")
class Truck(Vehicle):
    def display(self):
        print("----  Details of Truck are  ----")
        Vehicle.display(self)
        print()
class Car(Vehicle):
    def display(self):
        print("----  Details of Car are  ----")
        Vehicle.display(self)
        print()
class Motorcycle(Vehicle):
    def display(self):
        print("----  Details of Motorcycle are  ----")
        Vehicle.display(self)
        print()
obj = Truck("Truck","Blue",100)
obj.display()
obj1 = Car("BMW","Black",150)
obj1.display()
obj2 = Motorcycle("Ninja","Green",200)
obj2.display()

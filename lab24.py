'''Write a program to demonstrate hybrid inheritance and show MRO for each
class.'''
class Parent:
    def display(self):
        print("This is parent class")
#HIERARCHICAL INHERITANCE
class Child_1(Parent):
    def display1(self):
        Child_1.display(self) #or Parent.display(self)
        print("This is child 1")
        print()
class Child_2(Parent):
    def display1(self):
        Parent.display(self) #or Child_2.display(self)
        print("This is child 2")
        print()
#Multiple Inheritance
class Child_3(Child_1,Child_2):
    def display(self):
        Child_3.display1(self) #or Parent.display(self)
        print("This is Child 3")
        print()
obj = Child_1()
obj.display1()
obj1 = Child_2()
obj1.display1()
obj2 = Child_3()
obj2.display()


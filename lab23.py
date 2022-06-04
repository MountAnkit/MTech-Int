'''Write a program that extends the class Shape to calculate the area of a circle
and a cone .(use super to inherit base class methods)'''
class Shape:
    Pi = 3.14
    def __init__(self,radius):
        self.radius = radius
        print("Radius =",self.radius)
class Cone(Shape):
    def __init__(self,radius,height):
        super().__init__(radius)
        self.height = height
        print("Height =",self.height)
    def area(self):
        l = (self.height**2 + self.radius**2)**0.5
        area = (self.Pi * self.radius**2) + (self.Pi * self.radius*l)
        print("Area of Cone is :",area)
        print()
class Circle(Shape):
    def __init__(self,radius):
        super().__init__(radius)
    def area(self):
        area = (self.Pi * self.radius**2)
        print("Area of Circle is :",area)
        print()
obj = Cone(2,4)
obj.area()
obj1 = Circle(3)
obj1.area()


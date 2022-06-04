'''Write a program that has a class Polygon. Derive two classes Rectangle and
triangle from polygon and write methods to get the details of their dimensions
and hence calculate the area.'''
class Polygon:
    def __init__(self,dimension1,dimension2):
        self.d1 = dimension1
        self.d2 = dimension2
    def display(self):
        print(f"Dimension 1 = {self.d1}")
        print(f"Dimension 2 = {self.d2}")
        print()
        print("--- Area is ---")
class Rectangle(Polygon):
    def area(self):
        area = self.d1 * self.d2
        return area
    def display(self):
        print("--- Dimensions of Rectangle are ---")
        Polygon.display(self)
        print("Area =",Rectangle.area(self))
        print()
class Triangle(Polygon):
    def area(self):
        area = (self.d1 * self.d2) * 0.5
        return area
    def display(self):
        print("--- Dimensions of Triangle are ---")
        Polygon.display(self)
        print("Area =",Triangle.area(self))
        print()
obj = Rectangle(4,5)
obj.display()
obj1 = Triangle(4,5)
obj1.display()
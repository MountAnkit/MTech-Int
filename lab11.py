'''Write a program that has a class Point with attributes x and y.
a. Write a method called midpoint that returns a midpoint of a line joining two
points.
b. Write a method called length that returns the length of a line joining two
points.'''
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __sub__(self,o):
        a = self.x - o.x
        b = self.y - o.y
        return (a**2 + b**2)**0.5
    def __add__(self,o):
        a = self.x + o.x
        b = self.y + o.y
        return a/2,b/2
obj = point(3,4)
o = point(2,2)
mid = obj + o
legth = obj - o
print(mid)
print(legth)
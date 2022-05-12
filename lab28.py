'''WAP to create a Complex class having real and imaginary as it attributes.
Overload the +,-,/,* and += operators for objects of Complex class.'''
class Complex:
    def __init__(self,re,im):
        self.re = re
        self.im = im
    def show(self):
        print(self.re,self.im)
    def __add__(self,o):
        return Complex(self.re + o.re,self.im + o.im)
    def __sub__(self,o):
        return Complex(self.re - o.re,self.im - o.im)
    def __mul__(self,o):
        return Complex(self.re * o.re,self.im * o.im)
    def __truediv__(self,o):
        return Complex(self.re / o.re,self.im / o.im)
    def __iadd__(self,o):
        self.re = self.re + o.re
        self.im =  self.im + o.im
        return self
a = Complex(2,3j)
b = Complex(3,5j)
c = a+b
print(f"Sum = {c.re} + {c.im}")
d = a-b
print(f"Sub = {d.re} - {d.im}")
e = a*b
print(f"Mul = {e.re} * {e.im}")
f = a/b
print(f"Div = {f.re} + {f.im}")
a+=b
print(f"Iadd = {a.re} + {a.im}")


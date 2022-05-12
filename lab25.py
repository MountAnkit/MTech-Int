'''Write a program to overload + operator to multiply to fraction object of fraction
class which contain two instance variable numerator and denominator. Also,
define the instance method simplify() to simplify the fraction objects'''

def gcd(x,y):
  if y==0:
    return x
  else:
    return gcd(y,x%y)
class Fraction:
  def __init__(self,n,d):
    self.n = n
    self.d = d
  def __add__(self,other):
    self.a = self.n*other.n
    self.b = self.d*other.d
    c = Fraction(self.a,self.b)
    return c
  def simplify(self):
    g = gcd(self.n,self.d)
    self.n = self.n//g
    self.d = self.d//g
    print("{} / {}".format(self.n,self.d))
A = Fraction(5,2)
B = Fraction(5,5)
c = A+B
print(c.n,c.d)
c.simplify()
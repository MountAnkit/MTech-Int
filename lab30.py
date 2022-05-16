import inspect
import math
class A():
    def display(self):
        pass
class C(A):
    pass
def B(c):
    return c
print(inspect.isclass(A))
print(inspect.ismodule(math))
print(inspect.isfunction(B))
print(inspect.ismethod(math.gcd))
print(inspect.getmembers(math))
print(inspect.signature(math.pow))
print(inspect.getmodule(math))
print(inspect.getmro(C))
print(inspect.getdoc(math))
print(inspect.getsource(B))
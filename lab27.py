'''Write a program to overload inoperator'''
class ABC():
    def __init__(self,a):
        self.a = a
    def __contains__(self,o):
        if self.a in o.a:
            return "Yes"
        else:
            return "No"
obj = ABC(1)
obj1 = ABC([1,2,3])
c = obj.__contains__(obj1)
print(c)
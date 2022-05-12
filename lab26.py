'''Write a program to compare two-person object based on their age by
overloading > operator.'''
class compare:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __gt__(self,other):
        if self.age>other.age:
            return "Ankit older"
        else:
            return "Atul Older"
ob = compare("Ankit",17)
ob1 = compare("Atul",18)
c = ob>ob1
print(c)
class Name():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name : ",self.name)
        print("Age :",self.age)
class defin(Name):
    def hi(self):
        print("Details are:-")
        Name.display(self)
ob = defin("Ankit",17)
ob.hi()
print(type(ob))
print(id("abc"))
print(id("cba"))
print(isinstance(ob,Name))
print(issubclass(defin,Name))
print(callable(ob))
    

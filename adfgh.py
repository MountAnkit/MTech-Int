class Employee:
    N = 2
    name = ''
    designation = ''
    salary = ''
    counter = 0
    def getdata(self):
        self.name = input("Enter Name: ")
        self.designation = input("Enter Designation: ")
        self.salary = int(input("Enter Salary: "))
        Employee.counter = self.counter + self.salary
    def average(self):
        print("Average =",self.counter/self.N)
    def display(self):
        print("Name :",self.name)
        print("Designation :",self.designation)
        print("Salary :",self.salary)
obj1 = Employee()
obj1.getdata()
obj1.display()
obj2 = Employee()
obj2.getdata()
obj2.display()
obj2.average()


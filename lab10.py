class numbers:
    list1 = []
    def __init__(self):
        self.list1=[]
    def insert(self):
        a = int(input("Enter no of elements you want to enter: "))
        for i in range(a):
            b = int(input("Enter element: "))
            self.list1.append(b)
        numbers.list1 = self.list1
        print("List :",self.list1)
    @classmethod
    def find_max(cls):
        print(max(cls.list1))
obj = numbers()
obj.insert()
obj.find_max()
class Base: #Parent class
    def __init__(self):
        print("Parent class constructor called")
        self.a = "prashant" #public variable
        self.__c = "Ashish" #private variable
        
class Derived(Base): #Child class
    def __init__(self):
        Base.__init__(self) #calling parent class constructor
        # print("Child class constructor called")
        # print(self.a) #accessing parent class variable
        # print(self.__c) #accessing parent class private variable will give error   
        
obj1 = Derived()
print(obj1.a)
print(obj1.__c)
obj2 = Base()
print(obj2.a)
print(obj2.__c)

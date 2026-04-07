# how can we protect the functionailty of a class from outside world

class Rbi:
    #Declaring a public method
    def publicPolicy(self):
        print("RBI public policy is to control inflation and maintain price stability")
        
        #Declaring a private method
    def __privatePolicy(self):
        print("There is some pvt policy of RBI which is not disclosed to public")
        
class Sbi(Rbi):
    def __init__(self):     #first sbi class const called
        Rbi.__init__(self)  #second parent class const called
    
    def callingPublicMethod(self):   #child class public method
        print("\nInside child class public method")
        self.publicPolicy()  #calling parent class public method
        
    def callingPrivateMethod(self):  #child class public method
        self.__privatePolicy() #calling parent class private method will give error
        
obj1 = Sbi()
# obj1.callingPublicMethod()
# obj1.callingPrivateMethod() #calling private method will give error
obj1.publicPolicy() #calling parent class public method
obj1.__privatePolicy() #calling parent class private method will give error
# obj2 = Rbi()
# obj2.publicPolicy() #calling parent class public method
# obj2.__privatePolicy() #calling parent class private method will give error
# obj2 = Rbi()
# obj2.publicPolicy() #calling parent class public method
# obj2._Rbi_privatePolicy() #calling parent class private method using name 


        
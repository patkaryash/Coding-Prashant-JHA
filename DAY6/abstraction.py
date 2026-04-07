from abc import ABC, abstractmethod   
class Irctc(ABC):#abstract class  
  
    @abstractmethod  
    def bookTicket(self): # abstract method  
        pass  
  
class MakeMyTrip(Irctc):  
  
    def bookTicket(self):  
        print( "  ==========================================")  
        print("    Welcome To makemytrip   ")  
        source      = input("Enter a source station name:")  
        destination = input("Enter destination name:")  
        date        = input("Enter date:")  
        print( "  ==========================================")  
          
class GoIbibo(Irctc):  
      
    def bookTicket(self):  
        print("    Welcome To GOIBIBO")  
        source      = input("Enter a source station name:")  
        destination = input("Enter destination name:")  
        date        = input("Enter date:")  
  
class Yatra(Irctc):  
      
    def bookTicket(self):  
        print("    Welcome To Yatra  ")  
        source      = input("Enter a source station name:")  
        destination = input("Enter destination name:")  
        date        = input("Enter date:")  
  
m = MakeMyTrip()  
m.bookTicket()  
g = GoIbibo()  
g.bookTicket()  
y = Yatra()  
y.bookTicket()
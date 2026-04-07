import time
class Tower:
    def __init__(self, source):
        print("Welcome to Tower of Hanoi Game!")
        print()
        print("Given Problem     A=[3, 2, 1]   B=[]   C=[]")
        print()
        print("Expected Output   A=[]   B=[]   C=[3, 2, 1]")
        self.A = []   
        self.B = []         
        self.C = []          

    def tower(self,item):
        self.A.append(item)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A)
        print("Items in Tower A\n" )

    def pass1(self):
        self.temp = self.A.pop()
        self.C.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass One Completed==========================" )

    def pass2(self):
        self.temp = self.A.pop()
        self.B.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass Two Completed==========================" )

    def pass3(self):
        self.temp = self.C.pop()
        self.B.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass Three Completed==========================" )

    def pass4(self):
        self.temp = self.A.pop()
        self.C.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass Four Completed==========================" )

    def pass5(self):
        self.temp = self.B.pop()
        self.A.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass Five Completed==========================" )

    def pass6(self):
        self.temp = self.B.pop()
        self.C.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass Six Completed==========================" )

    def pass7(self):
        self.temp = self.A.pop()
        self.C.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass Seven Completed==========================" )
    
obj = Tower([3,2,1])
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()
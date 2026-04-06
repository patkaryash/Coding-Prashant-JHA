# class Arithmatic:  
#     def add(self,a):   # type: ignore
#         print(a)  
        
#     def add(self,a,b):   # type: ignore
#         print(a+b) 
         
#     def add(self,a,b,c):  
#         print(a+b+c) 
         
# obj = Arithmatic()  
# obj.add(10)   # type: ignore
# obj.add(10,20)   # type: ignore
# obj.add(1,2,3)  

# -------------------------------------------------------------------------------------

#To handle method overloading in python we can use default arguments
class Arithmatic:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None:
            print(a+b)
        elif a!=None and b!=None and c!=None:
            print(a+b+c)
        else:
            print("Enter atlest two arguements")

obj = Arithmatic()
obj.add(10)   # type: ignore
obj.add(10,20)   # type: ignore
obj.add(1,2,3)   # type: ignore

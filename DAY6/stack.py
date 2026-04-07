# Data structures are diiferent ways of organizing data in a computer memory that can be used effectively.
class Stack:
    def __init__(self):
        self.stacklist=[]

    def push(self,value):
        self.stacklist.append(value)

    def displaystack(self):
        print("----------------")
        print(self.stacklist)
        print("----------------")
        
    def isEmpty(self):
        if self.stacklist==[]:
            return True
        else:
            return False
        
stackobj = Stack()
while True:
   
    print("\n1. Push an element to stack")
    print("2.Pop an element from stack")
    print("3.Display stack")
    print("4.isEmpty")

    choice=int(input("Enter your choice: "))
    if choice==1:
        val=int(input("Enter the value for stack: "))
        stackobj.push(val)
    elif choice==2:
        if stackobj.stacklist:
            stackobj.stacklist.pop()
        else:
            print("Stack is empty!")
    elif choice==3:
        stackobj.displaystack()
    elif choice==4:
        print("Stack is empty:", stackobj.isEmpty())
    else:
        print("Invalid choice!")
        
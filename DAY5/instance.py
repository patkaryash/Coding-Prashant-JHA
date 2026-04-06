class Student:
    def __init__(self):
        self.s_name="Prashant"
        self.s_rollno=101  #declaring instance variable inside a constructor

    def getdata(self):
        self.s_mb = 8787878787 #

obj=Student()
obj.getdata()
del obj.s_name
obj.s_branch="CE" # pyright: ignore[reportAttributeAccessIssue]
print(obj.__dict__)
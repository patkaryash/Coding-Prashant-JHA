#polymorphism example
class Principal:
    def role(self):
        print("Principal=I am managing all activities of the college")

class Dean:
    def role(self):
        print("Dean=I am decision taking person of the college")

class Hod:
    def role(self):
        print("HOD=I am managing all the departments of the college")
        
class Faculty:
    def role(self):
        print("Faculty=I am teaching students of the college")
        
#-------------------class declaration completed------------------

def fun(obj):
    obj.role()   #calling method of class using object of class
campus=[Principal(), Dean(), Hod(), Faculty()]  #creating list of objects of different classes
for obj in campus:
    fun(obj)   #passing object of class to function
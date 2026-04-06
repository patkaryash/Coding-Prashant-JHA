class SubjMarks:    #class-1
    math = int(input("Enter marks for Math: "))
    DE = int(input("Enter marks for DE: "))
    c = int(input("Enter marks for C: "))
    english = int(input("Enter marks for English: "))

# --------------------------------------------------------------- parent class-1
class PractMarks:
    cpract = int(input("Enter marks for C practical: "))   
    
# --------------------------------------------------------------- parent class-2
class Result(SubjMarks, PractMarks):   #child class inheriting from both parent classes
    def total(self):
        if self.math>=40 and self.DE>=40 and self.c>=40 and self.english>=40 and self.cpract>=20:
            print("pass")
        else:
            print("fail")
            
obj = Result()   #creating object of child class
obj.total()   #accessing method of child class using child class object
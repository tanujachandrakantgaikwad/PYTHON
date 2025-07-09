#Write a python program to inherit (Derived class) “course“ from (base class) 
#“University”Using hybrid inheritance concept.
class University:
    def accpet(self):
        self.uname=input("ENter University name:")

class Student(University):
    def accepts(self):
        self.rno=int(input("Enter rno:"))
        self.name=input("Enter name:")
       

class Result(University):
    def acceptr(self):
        self.edate=input("Enter exam date:")
        self.per=float(input("Enter per:"))
       
class Course(Student,Result):
    def acceptc(self):
        self.cname=input("Enetr course name")
        self.ayear=int(input("Enter year"))
        print("Roll no=",self.rno)
        print("Name=",self.name)
        print(" Exam date=",self.edate)
        print("per=",self.per)
        print("cname=",self.cname)
        print("ayear=",self.ayear)


ob=Course()
ob.accepts()
ob.acceptr()
ob.acceptc()

                       
        

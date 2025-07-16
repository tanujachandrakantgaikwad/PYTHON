class College:
    def acceptc(self):
        self.cno=input("Enter college number: ")
        self.cname=input("Enter college name: ")
        self.addr=input("Enter college address: ")

class Student(College):
    def accepts(self):
        self.rno=input("Enter roll number: ")
        self.name=input("Enter student name: ")
        self.per=input("Enter percentage: ")

    def disp(self):
        print("College No =",self.cno)
        print("College Name =",self.cname)
        print("College Address =",self.addr)
    
        print("Student Roll No =",self.rno)
        print("Student Name =",self.name)
        print("Student Percentage =",self.per)

ob1=Student()
ob1.acceptc()
ob1.accepts()
ob1.disp()


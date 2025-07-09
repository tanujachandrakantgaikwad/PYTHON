class Emp:
    def accept(self):
        self.eno=input("enter emp no")
        self.ename=input("enter emp name")
        self.sal=input("enter emp sal")

    def disp(self):
        print("emp no=",self.eno)
        print("emp name=",self.ename)
        print("emp sal=",self.sal)

ob=Emp()
ob.accept()
ob.disp()

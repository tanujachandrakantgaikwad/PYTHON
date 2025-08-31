class InvalidDateException(RuntimeError):
    def _init_(self,msg):
        self.msg=msg

class Demo:
    def accept(self):
        self.dd=int(input("Enter dd:"))
        self.mm=input("Enter mm:")
        self.yy=input("Enter yy:")
    def disp(self):
        try:
            if not (self.dd>=1 and self.dd<=31):
                raise InvalidDateException("Date chukli....")
            print("Date=",self.dd,"/",self.mm,"/",self.yy)
        except InvalidDateException as e:
            print(e)

ob=Demo()
ob.accept()
ob.disp()

class Customer:
    def acceptc(self):
        self.cname=input("Enter name: ")
        self.phone_no=input("Enter phone no: ")
        

class Depositor(Customer):
    def acceptd(self):
        self.acc_no=input("Enter account number: ")
        self.bal=input("Enter balance: ")
        
class Borrower(Depositor):
    def acceptb(self):
        self.loan_no=input("Enter loan number: ")
        self.loan_amt=input("Enter loan amt: ")
      
    def disp(self):
    
        print("Customer Name =",self.cname)
        print(" phone no =",self.phone_no)
        print("account no =",self.acc_no)
        print("balance=",self.bal)
        print("loan no =",self.loan_no)
        print("loan amt =",self.loan_amt)
ob1=Borrower()
ob1.acceptc()
ob1.acceptd()
ob1.acceptb()
ob1.disp()


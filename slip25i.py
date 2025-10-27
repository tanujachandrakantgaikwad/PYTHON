class demo:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
ob=demo()
a=int(input("enter no 1"))
b=int(input("enter no 2"))
print("add=",ob.add(a,b))
print("sub=",ob.sub(a,b))
print("mul=",ob.mul(a,b))
print("div=",ob.div(a,b))

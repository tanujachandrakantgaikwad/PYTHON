#Write a python program to show the Hierarchical inheritance of two or moreclasses 
#named as “Square “ & “ Triangle” inherit from a single Base class as “Area “ .
class Area:
    def find_area(self):
     self.r=float(input("enter radius" ))
     self.a=3.14*self.r*self.r
     print("area of circle=",self.a)

class Square(Area):
    def find_Square(self):
        self.n=float(input("enter number" ))
        self.a=self.n*self.n
        print("area of square=",self.a)

class Triangle(Area):
    def find_triangle(self):
        self.b=float(input("enter breath" ))
        self.h=float(input("enter height" ))
        self.a=0.5*self.b*self.h
        print("area of triangle=",self.a)

ob=Triangle()
ob.find_area()
ob.find_triangle()

ob1=Square()
ob1.find_area()
ob1.find_Square()
        

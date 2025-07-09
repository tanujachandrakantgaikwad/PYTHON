#Define a class named Shape and its subclass (Square/Circle).
#The subclass has an init function which takes an argument (length/radius).
#Both classes have an area and volume  function which can print the area and
#volume of the shape where Shape's area is 0 by default.
class Shape:
    def __init__(self):
        self.a = 0

    def area(self):
        print("Area of shape =")

    def volume(self):
        print("Volume of shape =")


class Square(Shape):
    def __init__(self):
        super().__init__()
        self.s=float(input("Enter side of square: "))

    def area(self):
        self.a=self.s*self.s
        print("Area of square =",self.a)

    def volume(self):
        self.a=self.s*self.s*self.s
        print("Volume of square =",self.a)


class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.h=float(input("Enter height of cylinder: "))
        self.r=float(input("Enter radius of circle: "))

    def area(self):
        self.a=3.14*self.r*self.r
        print("Area of circle =",self.a)

    def volume(self):
        self.a=3.14*self.r*self.r*self.h
        print("Volume of cylinder",self.a)



ob1=Square()
ob1.area()
ob1.volume()


 ob2 = Circle()
 ob2.area()
 ob2.volume()




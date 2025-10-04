#Define a class named Shape and its subclass (Square/Circle). The subclass has an init 
#function which takes an argument (length/radius). Both classes have an areaand volume  
#function which can print the area and volume of the shape where Shape's areais 0 by 
#default.
class Shape:
    def area(self):
        print("Area: 0")   
    
    def volume(self):
        print("Volume: 0") 

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        print("Area of Square:", self.length * self.length)
    
    def volume(self):
        print("Volume of Cube:", self.length ** 3)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        print("Area of Circle:", 3.14 * self.radius * self.radius)
    
    def volume(self):
        print("Volume of Sphere:", (4/3) * 3.14 * self.radius ** 3)

shape = Shape()
shape.area()     
shape.volume()  

square = Square(4)
square.area()    
square.volume()  

circle = Circle(3)
circle.area()    
circle.volume()  

#Write a python program to show the Hierarchical inheritance of two or more
#classes named as “Square “ & “ Triangle” inherit from a single Base class as “Area “ .

class Area:
    def show_area_type(self):
        print("Calculating area...")

class Square(Area):
    def calculate_area(self, side):
        return side * side

class Triangle(Area):
    def calculate_area(self, base, height):
        return 0.5 * base * height

s = Square()
s.show_area_type()          
print("Area of Square:", s.calculate_area(4))

# Triangle
t = Triangle()
t.show_area_type()         
print("Area of Triangle:", t.calculate_area(5, 3))

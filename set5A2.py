#Write a Python program that defines a class named circle with attributes radius 
#and center, where center is a point object and radius is number. Accept center and 
#radius from user. Instantiate a circle object that represents a circle with its center 
#and radius as accepted input.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def display(self):
        print("Circle Center: (", self.center.x, ",", self.center.y, ")")
        print("Radius:", self.radius)

x = int(input("Enter center x: "))
y = int(input("Enter center y: "))
r = float(input("Enter radius: "))

center_point = Point(x, y)
c = Circle(center_point, r)

c.display()

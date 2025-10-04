# Write a python program to demonstrate single inheritance
#using findArea() function
# Parent class
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def findArea(self):
        return self.length * self.breadth


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


rect = Rectangle(10, 5)
print("Area of Rectangle:", rect.findArea())

sq = Square(6)
print("Area of Square:", sq.findArea())

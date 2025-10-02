# Define a class named Rectangle which can be constructed by a length and 
#width. The Rectangle class has a method which can compute the area and 
#volume.
class Rectangle:
    def __init__(self, length, width, height=0):
        self.length = length
        self.width = width
        self.height = height  

    def area(self):
        return self.length * self.width

    def volume(self):
        if self.height == 0:
            return "Height not provided, cannot calculate volume"
        return self.length * self.width * self.height

rect = Rectangle(5, 3)  
print("Area:", rect.area())
print("Volume:", rect.volume())  

rect3D = Rectangle(5, 3, 2)  
print("Area:", rect3D.area())
print("Volume:", rect3D.volume())

class Circle:
    def __init__(self, radius):  
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

r = float(input("Enter radius of the circle: "))

c = Circle(r)
print("Area:", c.area())
print("Circumference:", c.circumference())

# Write a Python Program to depict multiple inheritance when method is
#overridden in both classes and check the output accordingly.
class Parent1:
    def show(self):
        print("This is Parent1")

class Parent2:
    def show(self):
        print("This is Parent2")

class Child(Parent1, Parent2):
    def show(self):
        print("This is Child")

c = Child()
c.show()  

Parent1.show(c)  
Parent2.show(c)  

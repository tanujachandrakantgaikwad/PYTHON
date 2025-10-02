#Write a python program using simple class having class name as Student.
class Student:
    def __init__(self, name, roll_no):
        self.name=name
        self.roll_no=roll_no

    def display(self):
        print("Student Name:",self.name)
        print("Roll Number:",self.roll_no)

s1=Student("Tanuja", 101)
s1.display()

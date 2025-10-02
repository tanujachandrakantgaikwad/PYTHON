# Write a python program for parameterized constructor has multiple parameters along 
#with the self Keyword.
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name        
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)

s1=Student("Tanuja", 101, 85)
s2=Student("om", 102, 90)

s1.display()
print("-----")
s2.display()

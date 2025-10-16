#Write a python script to define a class student having members roll no,
#name, age, gender. Create a subclass called Test with member marks of 3
#subjects. Create three objects of the Test class and display all the
#details of the student with total marks.
# Parent class
class Student:
    def __init__(self, roll_no, name, age, gender):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender

# Subclass
class Test(Student):
    def __init__(self, roll_no, name, age, gender, marks1, marks2, marks3):
        super().__init__(roll_no, name, age, gender)
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        self.total = marks1 + marks2 + marks3

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Marks:", self.marks1, self.marks2, self.marks3)
        print("Total Marks:", self.total)
        print("------------------------")

# Create 3 objects
student1 = Test(1, "Tanuja", 20, "Female", 85, 90, 95)
student2 = Test(2, "Ravi", 21, "Male", 78, 88, 82)
student3 = Test(3, "Neha", 19, "Female", 92, 80, 87)

# Display details
student1.display()
student2.display()
student3.display()

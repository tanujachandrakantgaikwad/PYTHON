#Write a Python Program to Accept, Delete and Display students details such as 
#Roll.No, Name, Marks in three subject, using Classes. Also display percentage of 
#each student.
class Student:
    def __init__(self, roll_no, name, m1, m2, m3):
        self.roll_no = roll_no
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def percentage(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.m1, self.m2, self.m3)
        print("Percentage:", self.percentage(), "%")
        print("--------------")


students = []  

students.append(Student(101, "Tanuja", 85, 90, 88))
students.append(Student(102, "Rahul", 78, 82, 80))


print("All Students:\n")
for s in students:
    s.display()

for s in students:
    if s.roll_no == 102:
        students.remove(s)
        break

print("After Deletion:\n")
for s in students:
    s.display()

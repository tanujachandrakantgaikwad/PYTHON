#Write a python program to inherit (Derived class) “course“ from (base class) 
#“University”    Using hybrid inheritance concept.

class University:
    def show_university(self):
        print("This is the University.")

class Department:
    def show_department(self):
        print("This is a Department.")


class Course(University, Department):
    def show_course(self):
        print("This is a Course.")

c = Course()
c.show_university()   
c.show_department()   
c.show_course()       

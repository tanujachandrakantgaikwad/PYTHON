#Write a python program that will show the simplest form of
#inheritance using info() function. 
# Parent class
class Person:
    def info(self):
        print("I am a Person.")

class Student(Person):
    def info(self):
        print("I am a Student.")

p = Person()
p.info()

s = Student()
s.info()

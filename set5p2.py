#Write a python program for Counting the number of students using more objects of a 
#class. 
class Student:
    count=0  

    def __init__(self,name):
        self.name=name
        Student.count +=1   

s1=Student("Tanuja")
s2=Student("Rahul")
s3=Student("Priya")

print("Total number of students:", Student.count)

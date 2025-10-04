#Write a python program to demonstrate multilevel inheritance by using Base
#class name as “Team” which inherits Derived class name as “Dev”.
# Base class
class Team:
    def info(self):
        print("This is the Team base class.")

class Dev(Team):
    def info(self):
        print("This is the Developer class, inherited from Team.")

class Tester(Dev):
    def info(self):
        print("This is the Tester class, inherited from Dev.")

t = Team()
t.info()

d = Dev()
d.info()

ts = Tester()
ts.info()

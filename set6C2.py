#Write a Python Program to describe a HAS-A Relationship(Composition). 
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()  
    
    def start_car(self):
        print("Car is starting...")
        self.engine.start()   

my_car = Car()
my_car.start_car()

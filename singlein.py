class Demo:
    def func1(self):
        print("i am a base class")

class Demo1(Demo):
    def func2(self):
        print("I am a drived calss")

ob=Demo1()
ob.func2()
ob.func1()

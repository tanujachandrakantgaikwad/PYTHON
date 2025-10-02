#Write a python class to accept a string and number n from user and display n 
#repetition of strings using by overloading * operator.
class MyString:
    def __init__(self, text):
        self.text = text

    def __mul__(self, n):
        return self.text * n

# Input from user
s = input("Enter a string: ")
n = int(input("Enter a number: "))

# Create object
my_str = MyString(s)


print("Result:", my_str * n)

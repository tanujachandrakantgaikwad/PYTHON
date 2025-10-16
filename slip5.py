#  Write a Python script using class, which has two methods get_String and 
#print_String. get_String accept a string from the user and print_String print the string in 
#upper case.
class demo:
    def get_String(self):
        self.text = input("Enter a string: ")  # get string from user

    def print_String(self):
        print("In Upper Case:", self.text.upper())  # print in uppercase

# Create object
ob = demo()
ob.get_String()
ob.print_String()

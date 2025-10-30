#Write a Python program to input a positive integer. Display correct message for 
#correct and incorrect input. (Use Exception Handling)
 # Custom exception class
class NegativeNumberException(Exception):
    def __init__(self, msg):
        self.msg = msg
 
try:
    n = int(input("Enter a positive integer: "))
    if n < 0:
        raise NegativeNumberException("Invalid number! Number cannot be negative.")
    print("Valid number =", n)
except NegativeNumberException as e:
    print("Error =", e)


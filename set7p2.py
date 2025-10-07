#Write a Python program to input a positive integer. Display correct message
#for correct and incorrect input.
# Program to check if input is a positive integer

try:
    num = int(input("Enter a positive integer: "))
    if num > 0:
        print("Correct number")
    else:
        print("Incorrect! Number ")
except ValueError:
    print("Incorrect input")

# Program to find the factorial of a number

# Taking input from the user
num = int(input("Enter a number: "))

# Initialize factorial value
fact = 1

# Check if the number is negative, zero, or positive
if num < 0:
    print("Sorry, factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print("The factorial of", num, "is", fact)

# Define a class Date(Day, Month, Year) with functions to accept and display
#it. Accept date from user. Throw user defined exception “invalidDateException”
#if the date is invalid.
class InvalidDateException(Exception):
    pass

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"Date: {self.day}/{self.month}/{self.year}")

try:
    d = int(input("Enter day: "))
    m = int(input("Enter month: "))
    y = int(input("Enter year: "))

    if m < 1 or m > 12 or d < 1 or d > 31:
        raise InvalidDateException("Invalid date entered!")

    date = Date(d, m, y)
    date.display()

except InvalidDateException as e:
    print(e)
except ValueError:
    print("Please enter numbers only.")


    

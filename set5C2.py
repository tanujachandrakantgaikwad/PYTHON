#Define datetime module that provides time object. Using this module write a program 
#that gets current date and time and print day of the week.
import datetime

now = datetime.datetime.now()

print("Current date and time:", now)

print("Day of the week:", now.strftime("%A"))

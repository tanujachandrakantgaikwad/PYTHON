#1)Write a Python program to print Calendar of specific month of input
#year using calendar module
import calendar
year=int(input("enter year"))
month=int(input("enter month"))
print(calendar.month(year, month))

#Write a Python script to display datetime in various formats using datetime module 
#a.Current date and time b.Current year c.Month of yeard.Week number of the year 
#e.Weekday of the week f.Day of year g.Day of the month h.Day of week
import calendar
now=datetime.datetime.now()
print("Current date and time:",now)

year=int(input("enter year"))
print(calendar.calendar(year))

month=int(input("enter month"))

day=int(input("enter day"))
print("Month of year=",calendar.month(year, month))

date=datetime.date(year, month,day)
week=date.isocalendar().week
print("Week number of the year=",week)

print("Weekday of the week=",calendar.datetime.date(year, month,day))

today=datetime.date.today()
print("Today's date is:",today)

day_of_month=today.day
print("Day of the month",day_of_month)


# write a python program that try  to access the array element whose index
#is out of bound and handle the corresponding exception.
# Simple program to handle array index out of bound exception

numbers = [10, 20, 30, 40]

try:
    print(numbers[5])
except IndexError:
    print("Error: Index out of range!")


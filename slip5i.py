#Write a python script to generate Fibonacci terms using generator function.
# Generator function for Fibonacci
# Fibonacci generator
def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

n = int(input("Enter number of terms: "))

for i in fib(n):
    print(i, end=" ")


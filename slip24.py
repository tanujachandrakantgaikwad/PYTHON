def prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print(n, "is not prime")
                break
        else:
            print(n, "is prime")
    else:
        print(n, "is not prime")

def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    print("Factorial of", n, "is", f)

# Main part
num = int(input("Enter a number: "))
prime(num)
fact(num)

#Write a generator function which generates prime numbers up to n.
def prime_generator(n):
    for num in range(2, n+1):
    
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:   
            yield num

# Example usage
n = int(input("Enter a number: "))
for p in prime_generator(n):
    print(p, end=" ")

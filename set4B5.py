#(both included) and the values are square of keys
def prime_generator(n):
    for num in range(2, n+1):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num

# Example
for p in prime_generator(50):
    print(p, end=" ")

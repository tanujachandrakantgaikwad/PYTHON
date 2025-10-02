# Write Python class to perform addition of two complex numbers using binary  + 
#operator overloading.
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real    # real part
        self.imag = imag    # imaginary part

    # This makes + work
    def __add__(self, other):
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return ComplexNumber(new_real, new_imag)

    # Print the complex number
    def display(self):
        print(self.real, "+", self.imag, "i")


# Create two complex numbers
c1 = ComplexNumber(3, 2)  # 3 + 2i
c2 = ComplexNumber(1, 7)  # 1 + 7i

# Add them
c3 = c1 + c2  # calls __add__ automatically

# Show result
c3.display()  # Output: 4 + 9 i

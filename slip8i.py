# Define the class
class demo:
    def get_String(self):
        self.text = input("Enter a string: ")

    def print_String(self):
        # Print the string in uppercase
        print("Uppercase:", self.text.upper())

    def reverse_words(self):
        # Reverse the string word by word and print in lowercase
        rev = ' '.join(self.text.split()[::-1])
        print("Reversed word by word in lowercase:", rev.lower())

# Create object of the class
ob = demo()

# Call methods
ob.get_String()
ob.print_String()
ob.reverse_words()

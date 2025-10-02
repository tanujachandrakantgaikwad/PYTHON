#Write a Python class which has two methods get_String and print_String. 
#get_String accept a string from the user and print_String print the string in upper 
#case. Further modify the program to reverse a string word by word and print it in 
#lower case.
class StringManipulator:
    def __init__(self):
        self.text = ""  

    def get_String(self):
        self.text = input("Enter a string: ")

    def print_String(self):
        print("Uppercase:", self.text.upper())

    def reverse_words_lowercase(self):
        words = self.text.split()          
        reversed_words = words[::-1]       
        reversed_text = ' '.join(reversed_words)  
        print("Reversed lowercase:", reversed_text.lower())

s = StringManipulator()
s.get_String()
s.print_String()
s.reverse_words_lowercase()


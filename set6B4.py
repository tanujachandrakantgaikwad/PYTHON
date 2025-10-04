#Python Program to Create a Class in which One Method Accepts a String from 
#the User and Another method Prints it. Define a class named Country which has 
#a method called print Nationality. Define subclass named state from Country 
#which has a method called print State . Write a method to print state, country and 
#nationality.

class Country:
    def __init__(self):
        self.country_name = ""
        self.nationality = ""
    
    def set_country_info(self):
        self.country_name = input("Enter Country Name: ")
        self.nationality = input("Enter Nationality: ")
    
    def print_nationality(self):
        print("Nationality:", self.nationality)


class State(Country):
    def __init__(self):
        super().__init__()  
        self.state_name = ""
    
    def set_state_info(self):
        self.state_name = input("Enter State Name: ")
    
    def print_state(self):
        print("State:", self.state_name)
    
    def print_all_info(self):
        print("Country:", self.country_name)
        print("State:", self.state_name)
        print("Nationality:", self.nationality)

s = State()
s.set_country_info()   
s.set_state_info()     
print("\n--- Information ---")
s.print_all_info()    

#Write a Python program to check if a given key already exists in a dictionary. If     
#key exists replace with another key/value pair. 
s = {"name": "Tanuja", "age": 20, "city": "Pune"}

key = "age"

if key in s:
    print("Key found! Replacing it...")
    s["year"] = 2025   # add new key/value
    del s[key]         # delete old key
else:
    print("Key not found.")

print("New dictionary:", s)

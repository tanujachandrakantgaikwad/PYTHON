#Write text file named test.txt that contains integers, characters and
#float numbers. Write a Python program to read the test.txt file.
#And print appropriate message using exception 
try:
    f1 = open("test.txt", "r")     
    for line in f1:
        data = line.strip()         
        try:
            num = int(data)
            print(f"Integer found: {num}")
        except ValueError:
            try:
                num = float(data)
                print(f"Float found: {num}")
            except ValueError:
                print(f"Character or string found: {data}")
    f1.close()
except FileNotFoundError:
    print("Error: File not found!")

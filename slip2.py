#Write a Python function that accepts a string and calculate the number of upper case 
#letters and lower case letters.  
#Sample String: 'The quick Brown Fox' 
#Expected Output:  
#No. of Upper case characters: 3 
#No. of Lower case characters: 13
def letters(s):
    c1 = 0
    c2 = 0
    for ch in s:
        if ch.isupper():
            c1+=1
        elif ch.islower():
            c2+=1
    print("Upper case:", c1)
    print("Lower case:", c2)
letters("The quick Brown Fox")    




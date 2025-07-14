#set{}
# Write a Python program to add and remove operation on set.
a={21,89,32,67,54}
print(a)
a.add(33)
print(a)
a.remove(21)
print(a)

#Write a Python program to do iteration over sets.
a={23,99,67,65}
for num in a:
    print(num)
    
#Write a Python program to find the length of a set.
t={"tanuja","disha","sayali","sai","ram"}
print("length of set=",len(t))

#tuple[]
#Write a Python program to create a tuple with numbers and print one item.
r=(32,43,87,78)
print(r)

# Write a Python script to add a key to a dictionary. 
#Sample Dictionary : {0: 10, 1: 20} 
#Expected Result : {0: 10, 1: 20, 2: 30} 
t={0: 10, 1: 20}
t[2]=30
print(t)

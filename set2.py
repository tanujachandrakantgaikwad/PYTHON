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

#1 Write a Python program to find maximum and the minimum value in a set. 
e={"tanuja","om","sai","disha"}
print(min(e))
print(max(e))

#2 Write a Python program to add an item in a tuple.
s=(34,67,78,43)
print(s)
s=list(s)
s[2]=99
s=tuple(s)
print(s)

#3 Write a Python program to convert a tuple to a string. 
s=("T","a","n","u","j","a")
s1=''.join(s)
print(s1)

#4 write a Python program to create an intersection of sets.
a={34,65,78,98}
b={34,12,43,78}
c=a&b
c=a.intersection(b)
print(c)

#5 Write a Python program to create a union of sets.
a={34,65,78,98}
b={34,12,43,78}
c=a|b
c=a.union(b)
print(c)

#6 Write a Python script to check if a given key already exists in a dictionary.
s={"p","php","j","java","c","cpp","py","python"}
t=input("enter key")
if t in s:
    print("key found")
else:
    print("not found")

#7 Write a Python script to sort (ascending and descending)a dictionary by value.
#s={"p","php","j","java","c","cpp","py","python"}
#print("ascending order")
#for a in sorted(s.values()):
    #print(a,s[a])
    #print()
    #print("descending order")
    #for a in sorted(s.values(),reverse=True):
     #   print(a,s[a])

#Write a Python program to create set difference and a symmetric difference.
a={2,5,7,89,87}
b={32,5,7,87,8}
d1=a-b
d2=a^b
print("frist set=",a)
print("second set=",b)
print("different=",d1)
print("symmetric difference=",d2)

# Write a Python program to create a list of tuples with the first element
#as the number and second element as the square of the number.
n=input("enter number")
a=[2,4,6,7,4,3,2]
b=list((n,n*n)for n in a)
print(b)

#Write a Python program to unpack a tuple in several variables. 
s=("Tanuja",20,"BBACA")
name,age,course=s
print("Name:",name)
print("Age:",age)
print("course:",course)

#Write a Python program to get the 4th element from front and
# 4th element from last of a tuple.
a=(10,34,65,78,76,43)
if len(a)>=4:
    f=a[3]      
    fe=a[-4]
    print("4th element from front:",f)
    print("4th element from end:",fe)
else:
    print("not found")

#Write a Python program to find the repeated items of a tuple.
a=(21,32,21,4,5,4,3,23)
t=set([r for r in a if a.count(r)>1])
print("Repeated items=")
print(t)

# Write a Python program to check whether an element exists within a tuple.
a=(23,65,78,76)
n=int(input("enter number to search"))
if n in a:
    print("number found")
else:
    print("not found")




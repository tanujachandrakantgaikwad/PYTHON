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

# Write a recursive function which print string in reverse order.
s="TANUJA"
rev=s[::-1]
print("reverse string=",rev)
print("*********************************")

# Write a python script using function to calculate  XY
def power(x,y):
    a=x**y
    return a
x=float(input("enter value of x:"))
y=float(input("enter value of y:"))
print(" x raise to y=",power(x,y))
print("*********************************")

#. Define a function that accept two strings as input and
#find union and intersection of them.
def un(s1,s2):
    s1=set(s1)
    s2=set(s2)
    union=s1.union(s2)
    intersection=s1.intersection(s2)
    print("Union of characters:",''.join(sorted(union)))
    print("Intersection of characters:",''.join(sorted(intersection)))
p=input("Enter first string: ")
q=input("Enter second string: ")
un(p, q)
print("******************************")

#Write a recursive function to calculate sum of digits of a given input number. 
def sum(n):
    if n==0:
        return 0
    else:
        d=n%10
        num=n//10
        return d+sum(num)

num=int(input("Enter a number:"))
print("Sum of digits:",sum(num))
print("******************************")

# Write a recursive function to calculate sum of digits of a giveninput number.
def generator(n):
    for i in range(0,n+1,2):
       yield i
       
n=int(input("enter number"))
print("even number up to n",n)
for num in generator(n):
   print(num)





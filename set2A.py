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

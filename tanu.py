#Write a recursive function to calculate sum of digits of a given
#input number.
 
def generator(n):
    for i in range(0,n+1,2):
       yield i
       
n=int(input("enter number"))
print("even number up to n",n)
for num in generator(n):
   print(num)
       



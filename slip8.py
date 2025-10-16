#Write a python script to find the repeated items of a tuple 
t=(3,2,5,7,8,3,2)
for val in t:
       if t.count(val)>1:
           print(val,":",t.count(val))

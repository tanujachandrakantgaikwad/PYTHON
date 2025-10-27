# Write a Python program to convert a tuple of string values to a tuple of integer 
#values.   Original tuple values: (('333', '33'), ('1416', '55')) 
      #        New tuple values: ((333, 33), (1416, 55))
t=(('333', '33'), ('1416', '55'))
new_t=tuple((int (a),int (b))for a,b in t)
print(t)
print(new_t)

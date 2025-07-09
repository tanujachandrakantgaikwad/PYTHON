t={"rno":34,"name":"om","marks":87.98}
print(t)

print(t["name"])

print(t.values())
print(t.keys())

t["birthdate"]="1-nov-2005"
print(t)

del t["marks"]
print(t)

val=t.pop('name')
print(t)
print("deleted value=",val)

val=t.popitem()
print(t)
print("deleted value=",val)

del t


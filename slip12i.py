s = 'thequickbrownfoxjumpsoverthelazydog'
for char in set(s):
    count = s.count(char)
    if count > 1:
        print(f"{char}-{count}", end=", ")

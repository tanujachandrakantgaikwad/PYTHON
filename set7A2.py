#Write a function called oops that explicitly raises a IndexError exception
#when called. Then write another function that calls oops inside a
#try/except statement to catch the error. 

def oops():
    raise IndexError("IndexError!")

def handle_error():
    try:
        oops()
    except IndexError as e:
        print("error:", e)

handle_error()

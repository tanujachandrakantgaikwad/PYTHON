#Change the oops function in question 4 from SET A to raise an exception you
#define yourself, called MyError, and pass an extra data item along with the
#exception. You may identify your exception with either a string or a class.
#Then, extend the try statement in the catcher function to catch this
#exception and its data in addition to IndexError, and print the extra data
#item. Finally, if you used a string for your exception, go back and 
#change it be a class instance.
import sys
import traceback

class MyError(Exception):
    def __init__(self, message, data):
        self.message = message
        self.data = data
        super().__init__(self.message)

def oops():
    raise MyError("This is my custom error!", 123)

def safe(func, *args):
    try:
        func(*args)
    except IndexError as e:
        print("Caught IndexError:", e)
    except MyError as e:
        print("Caught MyError:", e.message)
        print("Extra data:", e.data)
        print("Stack trace:")
        traceback.print_exc()
    except Exception:
     
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("Exception type:", exc_type.__name__)
        print("Exception value:", exc_value)
        print("Stack trace:")
        traceback.print_exc()

safe(oops)

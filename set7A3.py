#Change the oops function you just wrote to raise an exception you define
#yourself, called MyError, and pass an extra data item along with the
#exception. Then, extend the try statement in the catcher function to
#catch this exception and its data in addition to IndexError, and print the
#extra data item.

class MyError(Exception):
    def __init__(self, message, data):
        self.message = message
        self.data = data
        super().__init__(self.message)
        
def oops():
    raise MyError("This is my custom error!",404)

def handle_error():
    try:
        oops()
    except IndexError:
        print(" IndexError!")
    except MyError as e:
        print(" MyError:", e.message)
        print("Extra data:", e.data)
handle_error()

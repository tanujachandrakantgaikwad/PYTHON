#Define a custom exception class which takes a string message as attribute.

class MyException(Exception):
    def __init__(self, mes):
        self.mes = mes
        super().__init__(self.mes)

try:
    raise MyException("This is a custom error message.")
except MyException as e:
    print("Exception=", e)

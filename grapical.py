from tkinter import *
from tkinter import messagebox

def show():
    messagebox.showinfo("Alert", "Button Pressed!")


root = Tk()

b1= Button(root, text="Click Me", command=show)
b1.pack()

root.mainloop()

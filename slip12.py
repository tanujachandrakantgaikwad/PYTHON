# Write a Python GUI program to create a label and change the label font style (font 
#name, bold, size) using tkinter module.
from tkinter import *
def fontstyle():
    text = t1.get()
    l2.config(text=text, font=("Arial", 14))

def name():
    text = t1.get()
    l2.config(text=text.upper())

def boldq():
    text = t1.get()
    l2.config(text=text, font=("Arial", 14, "bold"))

def sizechange():
    text = t1.get()
    l2.config(text=text, font=("Arial", 25))
window=Tk()
window.geometry("500x600")
l1=Label(window,text="chang")
t1=Entry(window)
l2=Label(window,text="")

b1=Button(window,text="fontstyle",command=fontstyle)
b2=Button(window,text="name",command=name)
b3=Button(window,text="bold",command=boldq)
b4=Button(window,text="size",command=sizechange)
l1.pack(),t1.pack()
l2.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()

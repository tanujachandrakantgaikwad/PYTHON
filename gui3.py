

from tkinter import *
window=Tk()
window.geometry("300x200")
l1=Label(window,text="USER NAME",bg="pink",fg="green")
l2=Label(window,text="PASSWORD",bg="pink",fg="green")

t1=Entry(window)
t2=Entry(window)

l3=Button(window,text="SUBMIT",bg="red")
l4=Button(window,text="OK",bg="blue")

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
l2.grid(row=1,column=0)
t2.grid(row=1,column=1)
l3.grid(row=2,column=0)
l4.grid(row=3,column=0)

from tkinter import *
def Change():
    s1=t1.get()
    ans=(s1.upper())
    t2.delete(0,END)
    t2.insert(0,ans)
window=Tk()
window.geometry("500x500")
l1=Label(window,text="Enter String")
l2=Label(window,text="Upper Case")

t1=Entry(window)
t2=Entry(window)

b1=Button(window,text="ChangeLettter",command=Change)

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
l2.grid(row=1,column=0)
t2.grid(row=1,column=1)
b1.grid(row=2,column=0)

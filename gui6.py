from tkinter import *
def square():
      a=t1.get()
      a=int(a)
      c=a*a
      t2.delete(0,END)
      t2.insert(0,c)

window=Tk()
window.geometry("500x500")
l1=Label(window,text="Enter Number1")
l2=Label(window,text="Square")

t1=Entry(window)
t2=Entry(window)
b1=Button(window,text="squ",command=square)

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
l2.grid(row=1,column=0)
t2.grid(row=1,column=1)
b1.grid(row=2,column=0)

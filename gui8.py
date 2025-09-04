from tkinter import *
def AreaCylinder():
      r=t1.get()
      h=t2.get()
      r=float(r)
      h=float(h)
      ans=2*3.14*r*h
      t3.delete(0,END)
      t3.insert(0,ans)
def VolumeCylinder():
      r=t1.get()
      h=t2.get()
      r=float(r)
      h=float(h)
      ans=3.14*r*r*h
      t3.delete(0,END)
      t3.insert(0,ans)
window=Tk()
window.geometry("500x500")
l1=Label(window,text="Enter radius")
l2=Label(window,text="Enter height")
l3=Label(window,text="Result")

t1=Entry(window)
t2=Entry(window)
t3=Entry(window)

b1=Button(window,text="AC",command=AreaCylinder)
b2=Button(window,text="VC",command=VolumeCylinder)

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
l2.grid(row=1,column=0)
t2.grid(row=1,column=1)
l3.grid(row=2,column=0)
t3.grid(row=2,column=1)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)

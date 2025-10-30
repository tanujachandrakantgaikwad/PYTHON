from tkinter import *
def upper():
    text = t1.get()
    text=text.upper()
    t2.insert(0,text)  
  

window=Tk()
window.geometry("500x500")
l1=Label(window,text=" enter string")
l2=Label(window,text=" upper string")

t1=Entry(window)
t2=Entry(window)
b1=Button(window,text="upper",command=upper)
l1.pack(),t1.pack()
l2.pack(),t2.pack()
b1.pack()
window.mainloop()

from tkinter import *
def show():
   s=""
    if(chk1.get()):
        s=s+"Java"

    if(chk2.get()):
        s=s+"PHP"

    if(chk3.get()):
        s=s+"Python"

    t1.delete(0,END)
    t1.insert(0,s)

window=Tk()
chk1=IntVar()
chk2=IntVar()
chk3=IntVar()
window.geometry("500x600")

c1=Checkbutton(window,text="Java",variable=chk1)
c2=Checkbutton(window,text="PHP",variable=chk2)
c3=Checkbutton(window,text="Python",variable=chk3)
b1=Button(window,text="Submit",command=show)

t1=Entry(window)

c1.pack()
c2.pack()
c3.pack()
b1.pack()
t1.pack()

window.mainloop()

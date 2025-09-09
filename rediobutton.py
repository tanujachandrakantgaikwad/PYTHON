from tkinter import *
def show():
    if chk1.get():
        t1.insert(0," FeMale ")
    else:
        t1.insert(0," Male ")
        
window=Tk()
chk1=IntVar()
window.geometry("500x500")
r1=Radiobutton(window,text="Male",value=0,variable=chk1)
r2=Radiobutton(window,text="FeMale",value=1,variable=chk1)
b1=Button(window,text="submit",command=show)
t1=Entry(window)

r1.pack()
r2.pack()
b1.pack()
t1.pack()
window.mainloop()

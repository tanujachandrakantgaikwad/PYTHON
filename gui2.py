import tkinter
window=tkinter.Tk()
window.geometry("300x200")
l1=tkinter.Label(window,text="USER NAME",bg="pink",fg="green")
l2=tkinter.Label(window,text="PASSWORD",bg="pink",fg="green")

t1=tkinter.Entry(window)
t2=tkinter.Entry(window)

l3=tkinter.Button(window,text="SUBMIT")
l4=tkinter.Button(window,text="OK")

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
l2.grid(row=1,column=0)
t2.grid(row=1,column=1)
l3.grid(row=2,column=0)
l4.grid(row=3,column=0)

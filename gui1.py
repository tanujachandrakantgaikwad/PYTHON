import tkinter
window=tkinter.Tk()
window.geometry("500x500")
window.config(bg="pink")
l1=tkinter.Label(window,text="NAME:")
l1.pack()
t1=tkinter.Entry(window)
t1.pack()

l2=tkinter.Label(window,text="Mobile No:")
l2.pack()
t2=tkinter.Entry(window)
t2.pack()

l3=tkinter.Label(window,text="Gender")
l3.pack()
t3=tkinter.Entry(window)
t3.pack()

l4=tkinter.Label(window,text="Class")
l4.pack()
t4=tkinter.Entry(window)
t4.pack()

window.mainloop()

from tkinter import *
def Word():
    n=t1.get()
    word=" "
    for d in n:
        if d=="0":word+="Zero"
        elif d=="1":word+="One"
        elif d=="2":word+="Two"
        elif d=="3":word+="Three"
        elif d=="4":word+="Four"
        elif d=="5":word+="Five"
        elif d=="6":word+="Six"
        elif d=="7":word+="Seven"
        elif d=="8":word+="Eight"
        elif d=="9":word+="Nine"
    t2.delete(0,END)
    t2.insert(0,word)
    
window=Tk()
window.geometry("500x500")
l1=Label(window,text="Enter Number")
l2=Label(window,text="Word")

t1=Entry(window)
t2=Entry(window)

b1=Button(window,text="InWord",command=Word)

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
l2.grid(row=1,column=0)
t2.grid(row=1,column=1)
b1.grid(row=2,column=0)

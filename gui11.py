from tkinter import *
def Alter():
    s1=t1.get()
    result=""
    for ch in s1:
        if ch.islower():
            result+=ch.upper()
        elif ch.isupper():
            result+=ch.lower()
        elif ch.isdigit():
            result+="?"
        elif ch==" ":
            result+="*"
        else:
            result+=ch

    t2.delete(0,END)
    t2.insert(0,result)
            
window=Tk()
window.geometry("500x500")
l1=Label(window,text="Enter A Sentence")
l2=Label(window,text="Result")

t1=Entry(window)
t2=Entry(window)

b1=Button(window,text="AlterBox",command=Alter)

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
l2.grid(row=1,column=0)
t2.grid(row=1,column=1)
b1.grid(row=2,column=0)

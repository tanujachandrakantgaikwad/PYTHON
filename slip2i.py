#Write Python GUI program to create a digital clock with Tkinter to
#display the time. 
from tkinter import *
import time

root = Tk()
root.title("Digital Clock")

label = Label(root, font=("Arial", 50), bg="black", fg="white")
label.pack()

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)  

update_time()
root.mainloop()

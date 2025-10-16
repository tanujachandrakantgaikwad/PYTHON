#Write Python GUI program to take accept your birthdate and output your
#age when a button is pressed.
import tkinter as tk
from datetime import date

def age():
    y = int(e.get())
    tk.Label(root, text=f"Your age: {date.today().year - y}").pack()

root = tk.Tk()
tk.Label(root, text="Enter Birth Year:").pack()
e = tk.Entry(root); e.pack()
tk.Button(root, text="Show Age", command=age).pack()
root.mainloop()

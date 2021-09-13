from tkinter import *
import time

root = Tk()
root.geometry("200x200")
root.config(bg="sky blue")

l1 = Label(root,fg="dark blue",bg="sky blue",font=("ds-digital",21))
l1.place(x=40,y=60)

def digital_clock():
    time_live = time.strftime("%I:%M:%S %p")
    l1.config(text = time_live)
    l1.after(1000,digital_clock)

digital_clock()
root.mainloop()
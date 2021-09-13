from tkinter import *

root = Tk()
root.geometry("500x500")

def select():
    s1 = "YOUR SELECTED NUMBER IS=" +str(v.get())
    l1.config(text=s1)

v=IntVar()
s1 = Spinbox(root, textvariable=v ,from_ = 0,to=30)
s1.pack()

b1 = Button(root,text="SUBMIT", command=select)
b1.pack()

l1 = Label(root)
l1.pack()

root.mainloop()
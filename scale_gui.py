from tkinter import *

root = Tk()
root.geometry("400x400")

def select():
    s1 = "YOUR SELECTED NUMBER IS=" +str(v.get())
    l1.config(text=s1)

v=DoubleVar()
s1 = Scale(root,variable=v, from_=1,to=10,orient=HORIZONTAL)
s1.pack()

b1 = Button(root,text="SUBMIT", command=select)
b1.pack()

l1 = Label(root)
l1.pack()

root.mainloop()
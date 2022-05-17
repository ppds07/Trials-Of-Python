from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry("300x300")
root.config(bg="white")


labels = Label(root,text="Choose any subject",fg="blue",bg="white",font=("arial",18))
labels.place(x=40,y=120)
b1 = Button(root,text="Maths",fg="red",bg="white",font=("arial",15))
b1.place(x=10,y=10)

b2 = Button(root,text="Science",fg="red",bg="white",font=("arial",15))
b2.place(x=210,y=10)

b3 = Button(root,text="History",fg="red",bg="white",font=("arial",15))
b3.place(x=10,y=260)

b4 = Button(root,text="EVS",fg="red",bg="white",font=("arial",15))
b4.place(x=230,y=260)
root.mainloop()

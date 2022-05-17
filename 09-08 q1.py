from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")
root.config(bg="white")

name_label = Label(root,text="Name: ",bg="white",fg="red",font=("Arial",15))
name_label.place(x=30,y=30)
name_entry = Entry(root,width=30)
name_entry.place(x=140,y=35)

contact_label = Label(root,text="Contact No: ",bg="white",fg="red",font=("arial",15))
contact_label.place(x=30,y=80)
contact_entry = Entry(root,width=30)
contact_entry.place(x=140,y=85)

b1 = Button(root,text="Confirm",fg="red",bg="white",font=("Arial",15))
b1.place(x=70,y=130)

b2 = Button(root,text="Cancel",bg="white",fg="red",font=("arial",15),command=quit)
b2.place(x=190,y=130)

dt = Label(root,text="09/08/2021",fg="red",bg="white")
dt.place(x=330,y=380)
root.mainloop()
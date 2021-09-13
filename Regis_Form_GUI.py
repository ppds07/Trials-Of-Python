from tkinter import *
from tkinter import messagebox
root=Tk()

root.geometry("500x500")
root.config(bg="black")

def checking():
    if len(name_entry.get()) > 4 and name_entry.get().isalpha() and len(contact_entry.get()) == 10 and contact_entry.get().isdigit() and len(password_entry.get()) >8:
        messagebox.showinfo("DONE","REGISTRATION SUCCESSFUL")
    else:
        messagebox.showwarning("INCORRECT","REGISTRATION UNSUCCESSFUL")

heading_label = Label(root,text="REGISTRATION FORM",font=("arial",25,"bold"),fg="white",bg="black")
heading_label.place(x=100,y=10)

name_label = Label(root,text="Name: ", font=("arial",15,"bold"),fg="white",bg="black")
name_label.place(x=60,y=90)
name_entry = Entry(root,width="25")
name_entry.place(x=180,y=90)

contact_label = Label(root,text="Contact: ",font=("arial",15,"bold"),fg="white",bg="black")
contact_label.place(x=60,y=120)
contact_entry = Entry(root, width="25")
contact_entry.place(x=180,y=120)

password_label = Label(root,text="Password: ",font=("arial",15,"bold"),fg="white",bg="black")
password_label.place(x=60,y=150)
password_entry = Entry(root,width="25")
password_entry.place(x=180,y=150)

b1 = Button(root,text="SUBMIT",font=("arial",18),command=checking)
b1.place(x=120,y=180)

b2 = Button(root,text="CANCEL",font=("arial",18),command=quit)
b2.place(x=240,y=180)

root.mainloop()
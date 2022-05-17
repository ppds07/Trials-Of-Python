from tkinter import *
from tkinter import messagebox
root1=Tk()

root1.geometry("300x300")
root1.config(bg="black")

pas=StringVar()
nam=StringVar()
def registration():
    root = Tk()

    root.geometry("500x500")
    root.config(bg="black")
    def checking1():
        if name_entry1.get() and contact_entry1.get() and password_entry1.get():
            messagebox.showinfo("DONE", "REGISTRATION SUCCESSFUL")
        else:
            messagebox.showerror("INCORRECT", "REGISTRATION UNSUCCESSFUL")

    heading_label1 = Label(root, text="REGISTRATION FORM", font=("arial", 25, "bold"), fg="white", bg="black")
    heading_label1.place(x=100, y=10)

    name_label1 = Label(root, text="Name: ", font=("arial", 15, "bold"), fg="white", bg="black")
    name_label1.place(x=60, y=90)
    nam=StringVar()
    name_entry1 = Entry(root, width="25",textvariable=nam)
    name_entry1.place(x=180, y=90)

    contact_label1 = Label(root, text="Contact: ", font=("arial", 15, "bold"), fg="white", bg="black")
    contact_label1.place(x=60, y=120)
    contact_entry1 = Entry(root, width="25")
    contact_entry1.place(x=180, y=120)

    password_label1 = Label(root, text="Password: ", font=("arial", 15, "bold"), fg="white", bg="black")
    password_label1.place(x=60, y=150)
    pas=StringVar()
    password_entry1 = Entry(root, width="25",textvariable=pas)
    password_entry1.place(x=180, y=150)

    b1 = Button(root, text="SUBMIT", font=("arial", 18), command=checking1)
    b1.place(x=120, y=180)

    b2 = Button(root, text="CANCEL", font=("arial", 18),command=quit)
    b2.place(x=240, y=180)

def login():
    root3 = Tk()
    root3.geometry("500x500")
    root3.config(bg="black")

    heading_label2 = Label(root3, text="LOGIN PORTAL", font=("arial", 25, "bold"), fg="white", bg="black")
    heading_label2.place(x=100, y=10)

    name_label2 = Label(root3, text="Name: ", font=("arial", 15, "bold"), fg="white", bg="black")
    name_label2.place(x=60, y=90)

    v1=StringVar()
    name_entry2 = Entry(root3, width="25",textvariable=v1)
    name_entry2.place(x=180, y=90)

    password_label2 = Label(root3, text="Password: ", font=("arial", 15, "bold"), fg="white", bg="black")
    password_label2.place(x=60, y=150)

    v2=StringVar()
    password_entry2 = Entry(root3, width="25",textvariable=v2)
    password_entry2.place(x=180, y=150)

    def checking2():
        if v1.get() == nam.get() and v2.get() == pas.get():
            messagebox.showinfo("DONE", "LOGIN SUCCESSFUL")
        else:
            messagebox.showerror("INCORRECT", "LOGIN UNSUCCESSFUL")


    b3= Button(root3, text="SUBMIT", font=("arial", 18), command=checking2)
    b3.place(x=120, y=180)

    b4 = Button(root3, text="CANCEL", font=("arial", 18),command=quit)
    b4.place(x=240, y=180)

b5 = Button(root1,text="Registration",command = registration)
b5.place(x=130,y=120)

b6 = Button(root1,text="Login",command = login)
b6.place(x=130,y=180)

root1.mainloop()
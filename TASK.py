from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("400x400")

var1=StringVar()
var2=StringVar()
def login():
    root3 = Tk()
    root3.geometry("400x400")
    l1 = Label(root3, text="LOGIN FORM")
    l1.pack()

    log_1 = Label(root3, text="NAME")
    log_1.pack()

    v=StringVar()
    log_e1 = Entry(root3, width=25,textvariable=v)
    log_e1.pack()

    log_2 = Label(root3, text="PASSWORD")
    log_2.pack()

    v2=StringVar()
    log_e2 = Entry(root3, width=25,textvariable=v2)
    log_e2.pack()

    def checking():
        if v.get() == var1.get() and v2.get() == var2.get():
            messagebox.showinfo("CORRECT", "LOGIN SUCCESSFUL")
        else:
            messagebox.showinfo("WRONG", "LOGIN FAILED")

    log_b1 = Button(root3, text="LOGIN", command=checking)
    log_b1.pack()

    log_b2 = Button(root3, text="CANCEL")
    log_b2.pack()

def register():
    root2=Tk()
    root2.geometry("400x400")
    l1=Label(root2,text="REGISTRATION FORM")
    l1.pack()

    reg_1=Label(root2,text="NAME")
    reg_1.pack()

    var1=StringVar()
    reg_e1=Entry(root2,width=25,textvariable=var1)
    reg_e1.pack()

    reg_2 = Label(root2, text="PASSWORD")
    reg_2.pack()

    var2=StringVar()
    reg_e2 = Entry(root2, width=25,textvariable=var2)
    reg_e2.pack()

    def checking2():
        if reg_e1.get() and reg_e2.get():
            messagebox.showinfo("CORRECT","REGISTRATION SUCCESSFUL")
        else:
            messagebox.showerror("WRONG","TRY AGAIN")
    reg_b1=Button(root2,text="REGISTER",command=checking2)
    reg_b1.pack()

    reg_b2=Button(root2,text="CANCEL")
    reg_b2.pack()

b1=Button(root,text="REGISTER",command=register)
b1.pack()



b2=Button(root,text="LOGIN",command=login)
b2.pack()


root.mainloop()
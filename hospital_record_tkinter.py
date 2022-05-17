from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("400x400")

def doctor():
    root2=Tk()
    root2.geometry("400x400")
    def check():
        if e1.get():
            messagebox.showinfo("THANK YOU","YOU MAY PROCEED")
        else:
            messagebox.showerror("SORRY","PLEASE RETRY")
    d1=Label(root2,text="DOCTOR DASHBOARDD",font=("calibri",20),fg="red")
    d1.pack(side=TOP)
    d2=Label(root2,text="NAME:",font=("calibri",15),fg="blue")
    d2.place(x=30,y=70)
    e1=Entry(root2,font=("calibri",15),fg="blue")
    e1.place(x=170,y=70)
    d3=Label(root2,text="PRESCRIPTION",font=("calibri",15),fg="blue")
    d3.place(x=30,y=120)
    e2=Text(root2,font=("calibri",15),fg="blue",height=5,width=20)
    e2.place(x=170,y=120)
    db1=Button(root2,text="PROCEED",font=("calibri",15),fg="green",bg="orange",command=check)
    db1.place(x=50,y=270)
    db2=Button(root2,text="CANCEL",font=("calibri",15),fg="green",bg="orange",command=quit)
    db2.place(x=240,y=270)

def patient():
    root3=Tk()
    root3.geometry("400x400")
    def check():
        if e1.get() and e2.get() and e3.get()>(int(20)) and e4.get().isdigit() and e4.get()==10:
            messagebox.showinfo("THANK YOU","YOU MAY PROCEED NOW")
        else:
            messagebox.showerror("SORRY","TRY AGAIN LATER")
    p1=Label(root3,text="PATIENT DASHBOARD",font=("calibri",20),fg="red")
    p1.pack(side=TOP)
    p2=Label(root3,text="NAME:",font=("calibri",15),fg="blue")
    p2.place(x=30,y=70)
    e1=Entry(root3,font=("calibri",15),fg="blue")
    e1.place(x=170,y=70)
    p3=Label(root3,text="ILLNESS:",font=("calibri",15),fg="blue")
    p3.place(x=30,y=120)
    e2=Entry(root3,font=("calibri",15),fg="blue")
    e2.place(x=170,y=120)
    p4=Label(root3,text="WEIGHT:",font=("calibri",15),fg="blue")
    p4.place(x=30,y=190)
    e3=Entry(root3,font=("calibri",15),fg="blue")
    e3.place(x=170,y=190)
    p5=Label(root3,text="CONTACT.NO:",font=("calibri",15),fg="blue")
    p5.place(x=30,y=260)
    e4=Entry(root3,font=("calibri",15),fg="blue")
    e4.place(x=170,y=260)
    pb1 = Button(root3, text="PROCEED", font=("calibri", 15), fg="green", bg="orange",command=check)
    pb1.place(x=50, y=340)
    pb2 = Button(root3, text="CANCEL", font=("calibri", 15), fg="green", bg="orange", command=quit)
    pb2.place(x=240, y=340)


l1=Label(root,text="HOSPITAL MANAGEMENT SYSTEM",font=("arial black",15,"bold"),fg="red")
l1.pack(side=TOP)

b1=Button(root,text="DOCTOR LOGIN",font=("calibri",13),fg="blue",bg="pink",command=doctor)
b1.place(x=30,y=50)

b2=Button(root,text="NURSE LOGIN",font=("calibri",13),fg="blue",bg="pink")
b2.place(x=190,y=50)

b3=Button(root,text="PATIENT LOGIN",font=("calibri",13),fg="blue",bg="pink",command=patient)
b3.place(x=30,y=150)

b4=Button(root,text="ADMIN LOGIN",font=("calibri",13),fg="blue",bg="pink")
b4.place(x=190,y=150)

root.mainloop()
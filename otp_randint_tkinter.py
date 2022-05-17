from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.geometry("400x400")

global result


def window2():
    if len(e1.get()) > 3 and len(e2.get()) > 8 and len(e3.get()) == 10 and e3.get().isdigit() :
        root2=Tk()
        root2.geometry("600x100")
        l1 = Label(root2,text="OTP")
        l1.pack()
        #random otp
        a=1000
        b=9999
        result = random.randint(a,b)
        l2 = Label(root2)
        l2.config(text=result)
        l2.pack()
        b_otp = Button(root2,text="PROCEED",command=window3)
        b_otp.pack()
        #paste here the window3
        
    else:
        messagebox.showwarning("REGISTRATION PORTAL","TRY AGAIN")

def window3():
    root3 = Tk()
    root3.geometry("400x400")
    name=Label(root3,text="Name:")
    name.pack()
    namee=Label(root3,text=e1.get())
    namee.pack()

    emailid=Label(root3,text="Email ID:")
    emailid.pack()
    emailide=Label(root3,text=e2.get())
    emailide.pack()

    getotp = Label(root3,text="OTP: ")
    getotp.pack()
    getotpe = Entry(root3)
    getotpe.pack()

    def confirmation():
            if getotpe.get() == result:
                messagebox.showinfo("PURCHASE PORTAL","YOU CAN START PURCHASING")
            else:
                messagebox.showwarning("PURCHASE PORTAL","TRY AGAIN")

    b01 = Button(root3,text="CONFIRM",command=confirmation)
    b01.pack()
    b02 = Button(root3,text="QUIT",command=quit)
    b02.pack()



l1 = Label(root,text="Name")
l1.pack()

e1 = Entry(root)
e1.pack()

l2 = Label(root,text="EMAIL ID")
l2.pack()

e2 = Entry(root)
e2.pack()

l3 = Label(root,text="CONTACT NO")
l3.pack()

e3=Entry(root)
e3.pack()

b1 = Button(root,text="Submit",command=window2)
b1.pack()

b2 = Button(root,text="Cancel",command=quit)
b2.pack()

root.mainloop()

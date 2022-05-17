from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.config(bg="grey")

def check():
    if len(name_e.get()) > 5 and len(email_e.get()) > 8 and ref_e.get() == "7679823" and len(cn_e.get()) == 10 and cn_e.get().isdigit():
        messagebox.showinfo("SHOPPING PORTAL","SIGNUP SUCCESFUL")
    else:
        messagebox.showerror("SHOPPING PORTAL","TRY AGAIN WITH FULL INFO")

h1 = Label(root,text="SHOPPING WEBSITE",font=("code bold" , 20),bg="grey",fg="white")
h1.pack()

nv = StringVar()
name_l = Label(root,text="NAME:",font=("minecraft",15),bg="grey")
name_l.place(x=20,y=50)
name_e = Entry(root,width=30,textvariable=nv)
name_e.place(x=180,y=55)

eidv = StringVar()
email_l = Label(root,text="EMAIL ID:",font=("minecraft",15),bg="grey")
email_l.place(x=20,y=90)
email_e = Entry(root,width=30,textvariable=eidv)
email_e.place(x=180,y=95)

rv = StringVar()
ref_l = Label(root,text="REFERRAL:",font=("minecraft",15),bg="grey")
ref_l.place(x=20,y=130)
ref_e = Entry(root,width=30,textvariable=rv)
ref_e.place(x=180,y=135)

cnv = StringVar()
cn_l = Label(root,text="CONTACT NO:",font=("minecraft",15),bg="grey")
cn_l.place(x=20,y=170)
cn_e = Entry(root,width=30,textvariable=cnv)
cn_e.place(x=180,y=175)


b_submit = Button(root,text="SUBMIT",font=("code bold" , 15),bg="black",fg="red",command=check)
b_submit.place(x=100,y=230)

b_cancel = Button(root,text="CANCEL",font=("code bold" , 15),bg="black",fg="red",command=quit)
b_cancel.place(x=250,y=230)




root.mainloop()
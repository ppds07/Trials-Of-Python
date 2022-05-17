from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry("450x450")
root.config(bg="white")


def check():
    if name_entry.get() and sn_entry.get() == "amazon" or sn_entry.get() == "AMAZON" or sn_entry.get() == "Amazon" or sn_entry.get() == "FLIPKART" or sn_entry.get() == "flipkart" or sn_entry.get() == "Flipkart" or sn_entry.get() == "SHOPPIE" or sn_entry.get() == "shoppie" or sn_entry.get() == "Shoppie" or sn_entry.get() == "SNAPDEAL" or sn_entry.get() == "snapdeal" or sn_entry.get() == "Snapdeal":
          messagebox.showinfo("PORTAL", "Registration Successful")
    else:
        messagebox.showerror("PORTAL", "Wrong Store Name, Try Again !!")

amazon_b = Button(root,text="AMAZON",font=("arial",16),fg="red",bg="white")
amazon_b.place(x=10,y=0)

flipkart_b = Button(root,text="FLIPKART",font=("arial",16),fg="red",bg="white")
flipkart_b.place(x=330,y=0)

name_label = Label(root,text="NAME:",font=("arial",13),fg="blue",bg="white")
name_label.place(x=80,y=120)
name_entry = Entry(root,width=25)
name_entry.place(x=200,y=125)

sn_label = Label(root,text="STORE NAME:",font=("arial",13),fg="blue",bg="white")
sn_label.place(x=80,y=170)
sn_entry = Entry(root,width=25)
sn_entry.place(x=200,y=175)

confirm_b = Button(root,text="CONFIRM",font=("arial",13),fg="blue",bg="white",command=check)
confirm_b.place(x=130,y=230)

cancel_b = Button(root,text="CANCEL",font=("arial",13),fg="blue",bg="white")
cancel_b.place(x=260,y=230)

shoppie_b = Button(root,text="SHOPPIE",font=("arial",16),fg="red",bg="white")
shoppie_b.place(x=10,y=410)

snapdeal_b = Button(root,text="SNAPDEAL",font=("arial",16),fg="red",bg="white")
snapdeal_b.place(x=320,y=410)

root.mainloop()
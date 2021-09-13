from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry("500x500")
root.config(bg="white")


def check():
    if name_entry.get() and add_entry.get() and ph_entry.get() and pin_entry.get():
        messagebox.showinfo("Warning", "Order Successful")
    else:
        messagebox.showerror("Warning", "Type in all credentials")


def cancel():
    root.destroy()


heading_label = Label(root, text="SHOP WITH US", font=("arial bold", 20, "bold"), fg="red", bg="white")
heading_label.place(x=150, y=10)

name_label = Label(root, text="NAME:", font=("arial", 15), fg="blue", bg="white")
name_label.place(x=60, y=60)
name_entry = Entry(width=25)
name_entry.place(x=260, y=65)

ph_label = Label(root, text="CONTACT NO:", font=("arial", 15), fg="blue", bg="white")
ph_label.place(x=60, y=100)
ph_entry = Entry(root, width=25)
ph_entry.place(x=260, y=105)

add_label = Label(root, text="ADDRESS:", font=("arial", 15), fg="blue", bg="white")
add_label.place(x=60, y=140)
add_entry = Entry(root, width=25)
add_entry.place(x=260, y=145)

pin_label = Label(root, text="PINCODE:", font=("arial", 15), fg="blue", bg="white")
pin_label.place(x=60, y=180)
pin_entry = Entry(root, width=25)
pin_entry.place(x=260, y=185)

cancel_button = Button(root, text="CANCEL ORDER", command=cancel)
cancel_button.place(x=100, y=230)
confirm_button = Button(root, text="CONFIRM ORDER", command=check)
confirm_button.place(x=250, y=230)

root.mainloop()

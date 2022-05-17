from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry("700x700")
root.config(bg="white")


def check():
    if usr_entry.get() == 111 or usr_entry.get() == 112 or usr_entry.get() == 113 and pwd_entry.get() == 123 or pwd_entry.get() == 1234 or pwd_entry.get() == 1243:
          messagebox.showinfo("STUDENT PORTAL", "Login Successful")
    else:
        messagebox.showerror("STUDENT PORTAL", "Wrong credentials, Try Again !!")



heading_label = Label(root, text="LEARN WITH US", font=("arial bold", 30, "bold"), fg="black", bg="white")
heading_label.pack()

name_label = Label(root, text="LOGIN", font=("arial", 15), fg="red", bg="white")
name_label.place(x=60, y=60)


ph_label = Label(root, text="REGISTER", font=("arial", 15), fg="red", bg="white")
ph_label.place(x=140, y=60)

ph_label = Label(root, text="STUDENT PORTAL", font=("arial", 15), fg="red", bg="white")
ph_label.place(x=260, y=60)

ph_label = Label(root, text="TEACHERS PORTAL", font=("arial", 15), fg="red", bg="white")
ph_label.place(x=460, y=60)

usr_label = Label(root, text="Student ID :", font=("arial", 15), fg="blue", bg="white")
usr_label.place(x=200, y=140)
usr_entry = Entry(root, width=25)
usr_entry.place(x=330, y=145)

pwd_label = Label(root, text="Password :", font=("arial", 15), fg="blue", bg="white")
pwd_label.place(x=200, y=180)
pwd_entry = Entry(root, width=25)
pwd_entry.place(x=330, y=185)

cancel_button = Button(root, text="CANCEL ")
cancel_button.place(x=250, y=230)
confirm_button = Button(root, text="CONFIRM ", command=check)
confirm_button.place(x=400, y=230)

link_label = Label(root, text="www.learnwithus.com", fg="blue", bg="white")
link_label.place(x=580, y=670)

root.mainloop()

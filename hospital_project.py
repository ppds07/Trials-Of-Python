from tkinter import *
from tkinter import messagebox
import time
import random

root = Tk()
root.geometry("400x300")
root.config(bg="light blue")


def new_window2():
    root2 = Tk()
    root2.geometry("400x300")
    root2.config(bg="light blue")

    heading_label1 = Label(root2, text="Doctor's Dashboard", font=("calibri", 15, "bold"), bg="light blue")
    heading_label1.place(x=110, y=20)

    name_label = Label(root2, text="Name:", font=("calibri", 15), bg="light blue")
    name_label.place(x=30, y=60)

    name_entry = Entry(root2, width=25)
    name_entry.place(x=140, y=60)

    rep_label = Label(root2, text="Receipt No:", font=("calibri", 15), bg="light blue")
    rep_label.place(x=30, y=90)

    name_entry = Entry(root2, width=25)
    name_entry.place(x=140, y=92)

    prescription_label = Label(root2, text="Prescription:", font=("calibri", 15), bg="light blue")
    prescription_label.place(x=30, y=120)

    prescription_text = Text(root2, height=5, width=30)
    prescription_text.place(x=140, y=122)

    def ok():
        messagebox.showinfo("Thank You", "We have received the prescription")

    proceed_button = Button(root2, text="PROCEED", font=("calibri", 15, "bold"), command=ok)
    proceed_button.place(x=110, y=220)

    cancel_button = Button(root2, text="CANCEL", font=("calibri", 15, "bold"), command=quit)
    cancel_button.place(x=220, y=220)

    clock_label = Label(root2, fg="black", bg="light blue", font=("calibri", 12, "bold"))
    clock_label.place(x=310, y=10)

    def digital_clock():
        time_live = time.strftime("%I:%M:%S %p")
        clock_label.config(text=time_live)
        clock_label.after(1000, digital_clock)

    digital_clock()


def new_window3():
    root3 = Tk()
    root3.geometry("400x300")
    root3.config(bg="light blue")

    heading_label2 = Label(root3, text="Patient Dashboard", font=("calibri", 15, "bold"), bg="light blue")
    heading_label2.place(x=110, y=20)

    def check():
        if disease_entry.get().isalpha() and name_entry2.get().isalpha()  and len(contact_entry.get()) == 10 :
            messagebox.showinfo("Thank you", "we have received your response")
        else:
            messagebox.showerror("Portal", "Please fill the fields correctly")

    name_label2 = Label(root3, text="Name:", font=("calibri", 15), bg="light blue")
    name_label2.place(x=30, y=60)

    name_entry2 = Entry(root3, width=25)
    name_entry2.place(x=150, y=65)
    r1 = random.randint(1, 100)
    recipt_label = Label(root3,text =r1,font=("calibri", 15), bg="light blue" )
    recipt_label.place(x=10,y=10)

    disease_label = Label(root3, text="Disease:", font=("calibri", 15), bg="light blue")
    disease_label.place(x=30, y=100)

    disease_entry = Entry(root3, width=25)
    disease_entry.place(x=150, y=105)

    weight_label = Label(root3, text="Weight:", font=("calibri", 15), bg="light blue")
    weight_label.place(x=30, y=140)

    weight_entry = Entry(root3, width=25)
    weight_entry.place(x=150, y=145)

    contact_label = Label(root3, text="Contact No. :", font=("calibri", 15), bg="light blue")
    contact_label.place(x=30, y=180)

    contact_entry = Entry(root3, width=25)
    contact_entry.place(x=150, y=185)


    ok_button = Button(root3, text="OK", font=("calibri", 15), command=check)
    ok_button.place(x=130, y=230)

    cancel_button2 = Button(root3, text="CANCEL", font=("calibri", 15))
    cancel_button2.place(x=200, y=230)

    clock_label = Label(root3, fg="black", bg="light blue", font=("calibri", 12, "bold"))
    clock_label.place(x=310, y=10)

    def digital_clock():
        time_live = time.strftime("%I:%M:%S %p")
        clock_label.config(text=time_live)
        clock_label.after(1000, digital_clock)

    digital_clock()


def new_window4():
    root4 = Tk()
    root4.geometry("400x300")
    root4.config(bg="light blue")

    heading_label3 = Label(root4, text="Nurse Dashboard", font=("calibri", 15, "bold"), bg="light blue")
    heading_label3.place(x=110, y=20)

    def check():
        if name_entry2.get().isalpha() and work_entry.get() == "yes" or work_entry.get() == "YES" :
            messagebox.showinfo("Thank you", "You will receive your next help order soon")
        else:
            if name_entry2.get().isalpha() and work_entry.get() == "no" or work_entry.get() == "NO":
                messagebox.showinfo("Portal", "Kindly complete the order soon")
            else:
                messagebox.showerror("Portal","Kindly fill the details properly")

    name_label3 = Label(root4, text="Name:", font=("calibri", 15), bg="light blue")
    name_label3.place(x=30, y=60)

    name_entry2 = Entry(root4, width=25)
    name_entry2.place(x=150, y=65)

    repe_label = Label(root4, text="Receipt No:", font=("calibri", 15), bg="light blue")
    repe_label.place(x=30, y=100)

    weight_entry = Entry(root4, width=25)
    weight_entry.place(x=150, y=105)

    work_label = Label(root4, text="Work Done ?:", font=("calibri", 15), bg="light blue")
    work_label.place(x=30, y=140)

    work_entry = Entry(root4, width=25)
    work_entry.place(x=150, y=145)

    pres_label = Label(root4, text="Prescription:", font=("calibri", 15), bg="light blue")
    pres_label.place(x=30, y=180)

    pres_text = Text(root4, height=2, width=30)
    pres_text.place(x=150, y=185)

    ok_button = Button(root4, text="OK", font=("calibri", 15), command=check)
    ok_button.place(x=130, y=230)

    cancel_button2 = Button(root4, text="CANCEL", font=("calibri", 15),command=quit)
    cancel_button2.place(x=200, y=230)

    clock_label = Label(root4, fg="black", bg="light blue", font=("calibri", 12, "bold"))
    clock_label.place(x=310, y=10)

    def digital_clock():
        time_live = time.strftime("%I:%M:%S %p")
        clock_label.config(text=time_live)
        clock_label.after(1000, digital_clock)

    digital_clock()


def new_window5():
    root5 = Tk()
    root5.geometry("400x300")
    root5.config(bg="light blue")

    heading_label4 = Label(root5, text="Admin Dashboard", font=("calibri", 15, "bold"), bg="light blue")
    heading_label4.place(x=110, y=20)

    def check():
        if usr_entry.get().isalpha() and repe_entry.get() and pat_entry.get() and len(pat_entry.get()) == 10 :
            messagebox.showinfo("Portal", "The patient will soon receive the desired message entered ")
        else:
            messagebox.showerror("Portal","Kindly fill the details properly")

    usr_label = Label(root5, text="User ID:", font=("calibri", 15), bg="light blue")
    usr_label.place(x=30, y=60)

    usr_entry = Entry(root5, width=25)
    usr_entry.place(x=150, y=65)

    repe_label = Label(root5, text="Receipt No:", font=("calibri", 15), bg="light blue")
    repe_label.place(x=30, y=100)

    repe_entry = Entry(root5, width=25)
    repe_entry.place(x=150, y=105)

    pat_label = Label(root5, text="Patient Ph No:", font=("calibri", 15), bg="light blue")
    pat_label.place(x=30, y=140)

    pat_entry = Entry(root5, width=25)
    pat_entry.place(x=150, y=145)

    msg_label = Label(root5, text="Message:", font=("calibri", 15), bg="light blue")
    msg_label.place(x=30, y=180)

    pres_text = Text(root5, height=2, width=30)
    pres_text.place(x=150, y=185)

    ok_button = Button(root5, text="OK", font=("calibri", 15), command=check)
    ok_button.place(x=130, y=230)

    cancel_button2 = Button(root5, text="CANCEL", font=("calibri", 15),command=quit)
    cancel_button2.place(x=200, y=230)

    clock_label = Label(root5, fg="black", bg="light blue", font=("calibri", 12, "bold"))
    clock_label.place(x=310, y=10)

    def digital_clock():
        time_live = time.strftime("%I:%M:%S %p")
        clock_label.config(text=time_live)
        clock_label.after(1000, digital_clock)

    digital_clock()


heading_label = Label(root, text="HOSPITAL MANAGEMENT SYSTEM", font=("calibri", 16, "bold"), bg="light blue")
heading_label.place(x=55, y=25)

doctor_button = Button(root, text="Doctor's login", font=("calibri", 13, "bold"), fg="red", command=new_window2)
doctor_button.place(x=20, y=80)

nurse_button = Button(root, text="Nurse's login", font=("calibri", 13, "bold"), fg="red", command=new_window4)
nurse_button.place(x=140, y=80)

patient_button = Button(root, text="Patient's login", font=("calibri", 13, "bold"), fg="red", command=new_window3)
patient_button.place(x=260, y=80)

adminn_button = Button(root, text="Admin's login", font=("calibri", 13, "bold"), fg="red",command=new_window5)
adminn_button.place(x=140, y=140)

clock_label = Label(root, fg="black", bg="light blue", font=("calibri", 10, "bold"))
clock_label.place(x=315, y=5)


def digital_clock():
    time_live = time.strftime("%I:%M:%S %p")
    clock_label.config(text=time_live)
    clock_label.after(1000, digital_clock)


digital_clock()

root.mainloop()

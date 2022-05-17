from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")



def light_t():
    def check_light_order():
        if name_l_entry.get() and add_l_entry.get() and pin_l_entry.get() and ph_l_entry and itcode_l_entry.get():
            messagebox.showinfo("DELIVERY.COM", "THANKS FOR ORDERING")
        else:
            messagebox.showwarning("DELIVERY.COM", "PLEASE CHECK IF ALL BOXES ARE FILLED")

    def check_light_c():
        if name_l_c_entry.get() and code_l_c_entry.get():
            messagebox.showinfo("DELIVERY.COM", "COUPON APPLIED")
        else:
            messagebox.showwarning("DELIVERY.COM", "PLEASE CHECK IF ALL BOXES ARE FILLED")

    light = Tk()
    light.geometry("800x600")
    light.config(bg="white")

    label_light =  Label(light,text="DELIVERY.COM",font=("code bold",18),bg="white",fg="dark blue")
    label_light.pack()

    name_l = Label(light,text="NAME :",font=("code bold",15),bg="white")
    name_l.place(x=20,y=40)
    name_l_entry = Entry(light,width=25)
    name_l_entry.place(x=160,y=45)

    add_l = Label(light,text="ADDRESS :",font=("code bold",15),bg="white")
    add_l.place(x=20,y=80)
    add_l_entry = Entry(light,width=25)
    add_l_entry.place(x=160,y=85)

    pin_l = Label(light, text="PIN :", font=("code bold", 15), bg="white")
    pin_l.place(x=20, y=120)
    pin_l_entry = Entry(light, width=25)
    pin_l_entry.place(x=160, y=125)

    ph_l = Label(light, text="CONTACT NO :", font=("code bold", 15), bg="white")
    ph_l.place(x=20, y=160)
    ph_l_entry = Entry(light, width=25)
    ph_l_entry.place(x=160, y=165)

    itcode_l = Label(light, text="ITEM CODE :", font=("code bold", 15), bg="white")
    itcode_l.place(x=20, y=200)
    itcode_l_entry = Entry(light, width=25)
    itcode_l_entry.place(x=160, y=205)

    b_l_submit = Button(light,text="SUBMIT",font=("code bold",15),bg="white",fg="red",command=check_light_order)
    b_l_submit.place(x=30,y=250)

    b_l_cancel = Button(light, text="CANCEL", font=("code bold", 15), bg="white", fg="red")
    b_l_cancel.place(x=160, y=250)

    l_coupon = Label(light,text="COUPON DETAILS:",font=("code bold", 18), bg="white",fg="pink")
    l_coupon.place(x=380,y=40)

    name_l_c = Label(light, text="NAME :", font=("code bold", 15), bg="white")
    name_l_c.place(x=380, y=80)
    name_l_c_entry = Entry(light, width=25)
    name_l_c_entry.place(x=570, y=85)

    code_l_c = Label(light, text="COUPON CODE :", font=("code bold", 15), bg="white")
    code_l_c.place(x=380, y=120)
    code_l_c_entry = Entry(light, width=25)
    code_l_c_entry.place(x=570, y=125)

    age_l_c_label = Label(light,text="AGE :",font=("code bold", 15), bg="white")
    age_l_c_label.place(x=380,y=160)
    age_l_c_scale = Scale(light, from_=1, to=100, orient=HORIZONTAL)
    age_l_c_scale.place(x=570,y=165)

    b_l_applyc = Button(light, text="APPLY", font=("code bold", 15), bg="white", fg="red",command=check_light_c)
    b_l_applyc.place(x=460, y=220)

    b_l_cancelc = Button(light, text="CANCEL", font=("code bold", 15), bg="white", fg="red")
    b_l_cancelc.place(x=560, y=220)



def dark_t():

    def check_dark_order():
        if name_d_entry.get() and add_d_entry.get() and pin_d_entry.get() and ph_d_entry and itcode_d_entry.get():
            messagebox.showinfo("DELIVERY.COM", "THANKS FOR ORDERING")
        else:
            messagebox.showwarning("DELIVERY.COM", "PLEASE CHECK IF ALL BOXES ARE FILLED")

    def check_dark_c():
        if name_d_c_entry.get() and code_d_c_entry.get():
            messagebox.showinfo("DELIVERY.COM", "COUPON APPLIED")
        else:
            messagebox.showwarning("DELIVERY.COM", "PLEASE CHECK IF ALL BOXES ARE FILLED")

    dark = Tk()
    dark.geometry("800x600")
    dark.config(bg="black")

    label_dark = Label(dark,text="DELIVERY.COM",font=("code bold",18),bg="black",fg="sky blue")
    label_dark.pack()

    name_d = Label(dark,text="NAME :",font=("code bold",15),bg="black",fg="white")
    name_d.place(x=20,y=40)
    name_d_entry = Entry(dark,width=25)
    name_d_entry.place(x=160,y=45)

    add_d = Label(dark,text="ADDRESS :",font=("code bold",15),bg="black",fg="white")
    add_d.place(x=20,y=80)
    add_d_entry = Entry(dark,width=25)
    add_d_entry.place(x=160,y=85)

    pin_d = Label(dark, text="PIN :", font=("code bold", 15), bg="black",fg="white")
    pin_d.place(x=20, y=120)
    pin_d_entry = Entry(dark, width=25)
    pin_d_entry.place(x=160, y=125)

    ph_d = Label(dark, text="CONTACT NO :", font=("code bold", 15), bg="black",fg="white")
    ph_d.place(x=20, y=160)
    ph_d_entry = Entry(dark, width=25)
    ph_d_entry.place(x=160, y=165)

    itcode_d = Label(dark, text="ITEM CODE :", font=("code bold", 15), bg="black",fg="white")
    itcode_d.place(x=20, y=200)
    itcode_d_entry = Entry(dark, width=25)
    itcode_d_entry.place(x=160, y=205)

    b_d_submit = Button(dark,text="SUBMIT",font=("code bold",15),bg="light grey",fg="red",command=check_dark_order)
    b_d_submit.place(x=30,y=250)

    b_d_cancel = Button(dark, text="CANCEL", font=("code bold", 15), bg="light grey", fg="red")
    b_d_cancel.place(x=160, y=250)

    d_coupon = Label(dark,text="COUPON DETAILS:",font=("code bold", 18), bg="black",fg="pink")
    d_coupon.place(x=380,y=40)

    name_d_c = Label(dark, text="NAME :", font=("code bold", 15), bg="black",fg="white")
    name_d_c.place(x=380, y=80)
    name_d_c_entry = Entry(dark, width=25)
    name_d_c_entry.place(x=570, y=85)

    code_d_c = Label(dark, text="COUPON CODE :", font=("code bold", 15), bg="black",fg="white")
    code_d_c.place(x=380, y=120)
    code_d_c_entry = Entry(dark, width=25)
    code_d_c_entry.place(x=570, y=125)

    age_d_c_label = Label(dark,text="AGE :",font=("code bold", 15), bg="black",fg="white")
    age_d_c_label.place(x=380,y=160)
    age_d_c_scale = Scale(dark, from_=1, to=100, orient=HORIZONTAL)
    age_d_c_scale.place(x=570,y=165)

    b_d_applyc = Button(dark, text="APPLY", font=("code bold", 15), bg="light grey", fg="red",command=check_dark_c)
    b_d_applyc.place(x=460, y=220)

    b_d_cancelc = Button(dark, text="CANCEL", font=("code bold", 15), bg="light grey", fg="red")
    b_d_cancelc.place(x=560, y=220)



l1 = Label(root,text="Select Theme",font=("minecraft",20))
l1.pack()

b1 = Button(root,text="Dark",font=("minecraft",15),bg="black",fg="white",command=dark_t)
b1.place(x=40,y=80)

b2 = Button(root,text="Light",font=("minecraft",15),command=light_t)
b2.place(x=110,y=80)

root.mainloop()
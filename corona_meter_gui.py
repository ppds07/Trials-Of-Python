from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.config(bg="orange")

score = 0

h1 = Label(root,text="CORONA TEST ANALYZER",font=("minecraft",20),bg="orange")
h1.pack()

name = Label(root,text="Enter Your Name: ", font=("code bold",15),bg="orange")
name.place(x=10,y=50)
name_eb = Entry(root,width=20)
name_eb.place(x=320,y=50)

well = Label(root,text="Are You Feeling Well ?",font=("code bold",15),bg="orange")
well.place(x=10,y=80)
well_eb = Entry(root,width=20)
well_eb.place(x=320,y=80)

smell = Label(root,text="Can You Smell Food ?",font=("code bold",15),bg="orange")
smell.place(x=10,y=110)
smell_eb = Entry(root,width=20)
smell_eb.place(x=320,y=110)

taste = Label(root,text="Can You Taste Food ?",font=("code bold",15),bg="orange")
taste.place(x=10,y=140)
taste_eb = Entry(root,width=20)
taste_eb.place(x=320,y=140)

weight = Label(root,text="Are You Loosing Weight ?",font=("code bold",15),bg="orange")
weight.place(x=10,y=170)
weight_eb = Entry(root,width=20)
weight_eb.place(x=320,y=170)

age = Label(root,text="Age: ",font=("code bold",15),bg="orange")
age.place(x=10,y=200)
age_eb = Entry(root,width=20)
age_eb.place(x=320,y=200)

dia = Label(root,text="Do You Have Diabetes ?",font=("code bold",15),bg="orange")
dia.place(x=10,y=200)
dia_eb = Entry(root,width=20)
dia_eb.place(x=320,y=200)

b1 = Button(root,text="SUBMIT",font=("code bold",15),bg="black",fg="orange")
b1.place(x=120,y=250)

b2 = Button(root,text="CANCEL",font=("code bold",15),command=quit,fg="orange",bg="black")
b2.place(x=230,y=250)

def check():
    if well_eb.get() == "yes"


root.mainloop()
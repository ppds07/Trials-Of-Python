from tkinter import *

rslt = ""

root = Tk()
root.geometry("400x400")
root.config(bg="light grey")

inpt = StringVar()
e1 = Entry(root,textvariable=inpt)
e1.place(x=120,y=10)

b_1 = Button(root,text="  1  ",fg="white",bg="black")
b_1.place(x=50,y=30)

root.mainloop()
from tkinter import *

root = Tk()
root.geometry("300x300")
root.config(bg="black")

heading_l = Label(root,text="Names Of Countries",font=("code bold",18),fg="red")
heading_l.pack()

l1 = Listbox(root)
l1.insert(1,"INDIA")
l1.insert(2,"JAPAN")
l1.insert(3,"UNITED STATES OF AMERICA")
l1.insert(4,"SOUTH KOREA")
l1.insert(5,"UNITED KINGDOM")
l1.place(x=90,y=60)

root.mainloop()
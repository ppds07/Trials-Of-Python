from tkinter import *
root = Tk()
root.geometry("400x400")
root.config(bg="white")

name_label = Label(root,text="Name",fg="red",bg="white")
name_label.place(x=30,y=60)
name_entry = Entry(root,width=25)
name_entry.place(x=160,y=65)

gender_label = Label(root,text="Gender",fg="red",bg="white")
gender_label.place(x=30,y=130)

b1 = Radiobutton(root,text="Male")
b1.place(x=100,y=130)
root.mainloop()

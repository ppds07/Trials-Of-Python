from tkinter import*

root=Tk()
root.geometry("500x500")

j1=Label(root,text="JAVA", font=("arial black", 15), fg="blue")
j1.grid(row=0,column=0)

p1=Label(root, text="PYTHON", font=("arial black",15), fg="blue")
p1.grid(row=0,column=1)

j2=Label(root,text="1. Java is bit hard to understand", font=("calibri", 13),fg="red")
j2.grid(row=1,column=0)

p2=Label(root,text="1. Python is easy to understand", font=("calibri", 13),fg="red")
p2.grid(row=1,column=1)


j3=Label(root,text="2. The syntax is long", font=("calibri", 13),fg="red")
j3.grid(row=2,column=0)


p3=Label(root,text="2.Syntax is small", font=("calibri", 13),fg="red")
p3.grid(row=2,column=1)


j4=Label(root,text="3. Used less widely", font=("calibri", 13),fg="red")
j4.grid(row=3,column=0)


p4=Label(root,text="3.Used widely now", font=("calibri", 13),fg="red")
p4.grid(row=3,column=1)

root.mainloop()

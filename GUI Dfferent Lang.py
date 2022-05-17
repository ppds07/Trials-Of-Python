from tkinter import *
root = Tk()

root.geometry("500x500")
root.config(bg="white")
heading = Label(root,text="Different Programming Languages",fg="red")
heading.pack()

l1 = Label(root,text="1. Python",fg="blue")
l1.pack()
l2= Label(root,text="2. Java",fg="blue")
l2.pack()
l3 = Label(root,text="3. C",fg="blue")
l3.pack()
l4 = Label(root,text="4. C++",fg="blue")
l4.pack()
l5 = Label(root,text="5. PHP",fg="blue")
l5.pack()

q = Label(root,text="Is My Program Correct?")
q.pack()
b1 = Button(root,text="Yes")
b1.pack()
b2 = Button(root,text="No")
b2.pack()

root.mainloop()

from tkinter import *

root=Tk() # root is holding the tkinter

root.geometry("300x300")  #size of window
root.config(bg="black")
heading_label = Label(root,text="Welcome to GUI",fg = "white",bg="black")
heading_label.pack()

b1=Button(root, text="Submit")
b1.pack()

label1 = Label(root,text="1.Python",fg="white",bg="black")
label1.pack()
label2 = Label(root,text="2.Java",fg="white",bg="black")
label2.pack()

root.mainloop()
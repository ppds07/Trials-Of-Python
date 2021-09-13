from tkinter import *

root=Tk() # root is holding the tkinter

root.geometry("300x300")  #size of window
root.config(bg="black")
heading_label = Label(root,text="Welcome to GUI",fg = "white",bg="black")
heading_label.pack()

b1=Button(root, text="Submit")
b1.pack()


root.mainloop()
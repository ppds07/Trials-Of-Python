from tkinter import *
import webbrowser

root = Tk()
root.geometry("300x300")
root.config(bg="red")

def search():
    v1 = e1.get()
    webbrowser.open(v1)

l1 = Label(root,text="R3DLX SEARCH",font=("algerian",18))
l1.pack(side=TOP)

l2 = Label(root,text="Enter: ",font=("calibri",15))
l2.place(x=20,y=60)

e1 = Entry(root,width=24)
e1.place(x=100,y=65)

b1 = Button(root,text="SEARCH",command=search)
b1.place(x=80,y=120)

b2 = Button(root,text="QUIT",command=quit)
b2.place(x=160,y=120)

root.mainloop()
from tkinter import *
import requests as req

root = Tk()
root.geometry("500x500")

e1 = Entry(root)
e1.pack()

def checking():
    resp = e1.get()
    a=req.head(resp)
    ans =  "LAST MODIFIED" +a.headers['last-modified']
    root2=Tk()
    root2.geometry("500x500")
    l1 = Label(root2)
    l1.config(text=ans)
    l1.pack()

b1 = Button(root,text="Check",command=checking)
b1.pack()

root.mainloop()
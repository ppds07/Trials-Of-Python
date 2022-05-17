from tkinter import *

root = Tk()
root.geometry("400x400")

def submit():
    a = int(entry1.get())
    b = int(entry2.get())
    c = str(a+b)
    e1.insert(1,c)

a1 = PanedWindow()
a1.pack(fill = BOTH,expand=1)

e1 = Entry(a1)
a1.add(e1)

a2 = PanedWindow(a1,orient = VERTICAL)
a1.add(a2)

entry1 = Entry(a2)
entry2 = Entry(a2)

a2.add(entry1)
a2.add(entry2)

b1 = Button(a2,text="ADD",command=submit)
a2.add(b1)

def reset():
    entry1.delete(0,END)
    entry2.delete(0,END)
    e1.delete(0,END)

b2 = Button(a2,text="CLEAR",command=reset)
a2.add(b2)

root.mainloop()
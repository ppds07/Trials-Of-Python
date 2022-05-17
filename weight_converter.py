from tkinter import *
root = Tk()
def kgpoundgram():
    gram = float(e1.get())*1000
    pound = float(e1.get())*2.20462
    t1.delete("1.0",END)
    t1.insert(END,gram)
    t2.delete("1.0",END)
    t2.insert(END,pound)

l1 = Label(root,text="INPUT THE WEIGHT IN KG:")
l1.grid(row=0,column=0)

var1 = StringVar()
e1 = Entry(root,textvariable=var1)
e1.grid(row=0,column=1)

l2 = Label(root,text="GRAM")
l2.grid(row=1,column=0)

l3 = Label(root,text="POUND")
l3.grid(row=1,column=1)

t1 = Text(root,height=5,width=27)
t1.grid(row=2,column=0)

t2 = Text(root,height=5,width=27)
t2.grid(row=2,column=1)

b1 = Button(root,text="CONVERT",command=kgpoundgram)
b1.grid(row=3,column=1)

root.mainloop()
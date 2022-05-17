import pyspeedtest
from tkinter import *

root = Tk()
root.geometry("300x300")

def speed_test():
    ans = pyspeedtest.SpeedTest(e1.get())
    v1.set(ans.ping())
    v2.set(ans.download())
    v3.set(ans.upload())

l1 =Label(root,text="WEBSITE URL")
l1.pack()

e1 = Entry(root)
e1.pack()

v1 = StringVar()
l2 = Label(root,text="PING RESULT")
l2.pack()

r1 = Label(root,text="",textvariable=v1)
r1.pack()

v2 = StringVar()
l3 = Label(root,text="DOWNLOAD SPEED")
l3.pack()
r2 = Label(root,text="",textvariable=v2)
r2.pack()

v3 = StringVar()
l4 = Label(root,text="UPLOAD SPEED")
l4.pack()
r3 = Label(root,text="",textvariable=v3)
r3.pack()

b1 = Button(root,text="CHECK",command=speed_test)
b1.pack()

root.mainloop()
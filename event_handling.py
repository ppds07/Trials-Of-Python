from tkinter import *

root = Tk()
root.geometry("250x250")

def mouseclick(event):
    print("Right Button Clicked")

l1 = Button(root,text="Right Button")
l1.place(x=30,y=110)

l1.bind("<Button>",mouseclick)


def leftclick(event):
    print("Left Button Clicked")

l2 = Button(root,text="Left Button")
l2.place(x=150,y=110)
l2.bind("<Button>",leftclick)

root.mainloop()


from tkinter import *

#declare the variable

ex = ""

def press(num):
    global ex

    #concatenation:
    ex = ex + str(num)
    v1.set(ex)

def pressequal():

    try:
        global ex
        total = str(eval(ex))
        v1.set(total)
        ex=""


    except:
        v1.set("ERROR")
        ex=""


def clear():
    global ex 
    ex=""
    v1.set("")

#GUI Window
root = Tk()
root.configure(bg="red")
root.geometry("500x300")

v1=StringVar()
e1 = Entry(root,textvariable=v1)
e1.grid(row=0,column=2)

b1 = Button(root,text="1",fg="black",bg="white",font=("valorant",13),command=lambda:press(1),height=1,width=5)
b1.grid(row=1,column=1)

b2 = Button(root,text="2",fg="black",bg="white",font=("valorant",13),command=lambda:press(2),height=1,width=5)
b2.grid(row=1,column=2)

b3 = Button(root,text="3",fg="black",bg="white",font=("valorant",13),command=lambda:press(3),height=1,width=5)
b3.grid(row=1,column=3)

b4 = Button(root,text="4",fg="black",bg="white",font=("valorant",13),command=lambda:press(4),height=1,width=5)
b4.grid(row=2,column=1)

b5 = Button(root,text="5",fg="black",bg="white",font=("valorant",13),command=lambda:press(5),height=1,width=5)
b5.grid(row=2,column=2)

b6 = Button(root,text="6",fg="black",bg="white",font=("valorant",13),command=lambda:press(6),height=1,width=5)
b6.grid(row=2,column=3)

b7 = Button(root,text="7",fg="black",bg="white",font=("valorant",13),command=lambda:press(7),height=1,width=5)
b7.grid(row=3,column=1)

b8 = Button(root,text="8",fg="black",bg="white",font=("valorant",13),command=lambda:press(8),height=1,width=5)
b8.grid(row=3,column=2)

b9 = Button(root,text="9",fg="black",bg="white",font=("valorant",13),command=lambda:press(9),height=1,width=5)
b9.grid(row=3,column=3)

b0 = Button(root,text="0",fg="black",bg="white",font=("valorant",13),command=lambda:press(0),height=1,width=5)
b0.grid(row=4,column=2)

bequal = Button(root,text="=",fg="black",bg="white",font=(13),command=pressequal)
bequal.grid(row=4,column=3)

bplus = Button(root,text="+",fg="black",bg="white",font=("valorant",13),command=lambda:press("+"),height=1,width=5)
bplus.grid(row=1,column=4)

bsub = Button(root,text="-",fg="black",bg="white",font=("valorant",13),command=lambda:press("-"),height=1,width=5)
bsub.grid(row=2,column=4)

bmul = Button(root,text="x",fg="black",bg="white",font=("valorant",13),command=lambda:press("*"),height=1,width=5)
bmul.grid(row=3,column=4)

bdiv = Button(root,text="/",fg="black",bg="white",font=("valorant",13),command=lambda:press("/"),height=1,width=5)
bdiv.grid(row=4,column=4)

bclr = Button(root,text="clr",fg="black",bg="white",font=("valorant",13),command=clear)
bclr.grid(row=5,column=4)



root.mainloop()
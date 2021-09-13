from tkinter import *
import random

root = Tk()
root.geometry("400x400")
root.title("ROCK PAPER SCISSOR")

#computer value
values = {"0":"Rock", "1":"Paper","2":"Scissor"}

l1 = Label(root,text="ROCK PAPER SCISSOR")
l1.pack()

def reset_game():
    b1["state"]="active"
    b2["state"]="active"
    b3["state"]="active"
    l2.config(text="Player")
    l4.config(text="Computer")
    l5.config(text="")

def buttondisable():
    b1["state"]="disable"
    b2["state"]="disable"
    b3["state"]="disable"

def isrock():
    compvalue = values[str(random.randint(0,2))]
    if compvalue == "Rock":
        result="MATCH DRAW"
    elif compvalue == "Scissor":
        result = "Player Wins"
    else:
        result = "Computer Wins"
    l5.config(text=result)
    l2.config(text="Rock")
    buttondisable()

def ispaper():
    compvalue = values[str(random.randint(0,2))]
    if compvalue == "Paper":
        result="MATCH DRAW"
    elif compvalue == "Rock":
        result = "Player Wins"
    else:
        result = "Computer Wins"
    l5.config(text=result)
    l2.config(text="Paper")
    buttondisable()

def isscissor():
    compvalue = values[str(random.randint(0,2))]
    if compvalue == "Scissor":
        result="MATCH DRAW"
    elif compvalue == "Rock":
        result = "Player Wins"
    else:
        result = "Computer Wins"
    l5.config(text=result)
    l2.config(text="Scissor")
    buttondisable()

#Frame 1
f1=Frame(root)
f1.pack()

l2 = Label(f1,text="Player")
l2.pack()

l3 = Label(f1,text="VS")
l3.pack()

l4 = Label(f1,text="Computer")
l4.pack()

l5 = Label(root,text="")
l5.pack()

#Frame 2

f2 = Frame(root)
f2.pack()

b1 = Button(f2,text="Rock",command=isrock)
b1.pack()

b2 = Button(f2,text="Paper",command=ispaper)
b2.pack()

b3 = Button(f2,text="Scissor",command=isscissor)
b3.pack()

b4 = Button(root,text="Reset",command=reset_game)
b4.pack()

root.mainloop()